delimiter //
create procedure validTransaction(
in p_cid int, in p_mid int, in p_amount decimal(10,2)
)
begin
	declare v_bal decimal(10,2);
    declare exit handler for sqlexception 
	begin 
		rollback;
		select 'Error: Transaction rolled back due to exception' as Message;
	end;
	start transaction;
    -- check transaction
    select balance into v_bal from creditcard where CardID = p_cid;
    if v_bal is null then
		signal sqlstate '45000' set message_text = 'card not found';
	elseif v_bal < p_amount then
		signal sqlstate '45000' set message_text = 'insufficient balance';
	end if;
	-- deudct
	update creditcard set balance = balance-p_amount where CardID = p_cid;
	-- update merchant
	update merchant set AccountBalance = AccountBalance + p_amount where MerchantID = p_mid;
    -- record transaction
    insert into transactions(CardID, MerchantID, Amount, Status) values (p_cid,p_mid,p_amount,'Success');
	commit;
end //
delimiter ;