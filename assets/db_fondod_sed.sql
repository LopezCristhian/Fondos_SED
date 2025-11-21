CREATE TABLE institutions (
  id_institution SERIAL  NOT NULL ,
  name VARCHAR(20)   NOT NULL ,
  created_at DATETIME   NOT NULL ,
  updated_at DATETIME   NOT NULL   ,
PRIMARY KEY(id_institution));




CREATE TABLE expense_accounts (
  id  SERIAL  NOT NULL ,
  id_budget_code_expenses CHAR(5)   NOT NULL ,
  account_name VARCHAR(20)   NOT NULL ,
  created_at DATETIME   NOT NULL ,
  updated_at DATETIME   NOT NULL   ,
PRIMARY KEY(id ));




CREATE TABLE source_resoureces (
  id SERIAL  NOT NULL ,
  source_name VARCHAR(20)   NOT NULL ,
  created_at DATETIME   NOT NULL ,
  updated_at DATETIME   NOT NULL   ,
PRIMARY KEY(id));




CREATE TABLE budget_item_revenue (
  id SERIAL  NOT NULL ,
  code VARCHAR(10)   NOT NULL ,
  level CHAR   NOT NULL ,
  type_r ENUM   NOT NULL ,
  account_name VARCHAR(20)   NOT NULL ,
  father VARCHAR(10)    ,
  created_at DATETIME   NOT NULL ,
  updated_at DATETIME   NOT NULL   ,
PRIMARY KEY(id));




CREATE TABLE accountant_puc (
  id SERIAL  NOT NULL ,
  code VARCHAR(10)   NOT NULL ,
  name VARCHAR(20)   NOT NULL ,
  nature ENUM   NOT NULL ,
  father VARCHAR(20)    ,
  type_a ENUM   NOT NULL ,
  level  TINYINT    ,
  created_at DATETIME   NOT NULL ,
  updated_at DATETIME   NOT NULL   ,
PRIMARY KEY(id));




CREATE TABLE bank (
  id  CHAR   NOT NULL ,
  bank_name VARCHAR(20)   NOT NULL ,
  created_at DATETIME   NOT NULL ,
  updated_at DATETIME   NOT NULL   ,
PRIMARY KEY(id ));




CREATE TABLE budget_item_expenses (
  id SERIAL  NOT NULL ,
  code VARCHAR(10)   NOT NULL ,
  level CHAR(5)   NOT NULL ,
  type_e ENUM   NOT NULL ,
  account_name VARCHAR(20)   NOT NULL ,
  father VARCHAR(10)    ,
  created_at DATETIME   NOT NULL ,
  updated_at DATETIME   NOT NULL   ,
PRIMARY KEY(id));




CREATE TABLE revenue_budget (
  id CHAR   NOT NULL ,
  budget_item_revenue_id CHAR   NOT NULL ,
  period VARCHAR(20)   NOT NULL ,
  initial_appropriation DECIMAL(14, 2)   NOT NULL ,
  final_appropriation DECIMAL(14, 2)   NOT NULL ,
  created_at DATETIME   NOT NULL ,
  updated_at DATETIME   NOT NULL   ,
PRIMARY KEY(id)  ,
  FOREIGN KEY(budget_item_revenue_id)
    REFERENCES budget_item_revenue(id));


CREATE INDEX revenue_budget_FKIndex1 ON revenue_budget (budget_item_revenue_id);


CREATE INDEX IFK_Tiene ON revenue_budget (budget_item_revenue_id);


CREATE TABLE f1_format (
  id SERIAL  NOT NULL ,
  accountant_puc_id CHAR   NOT NULL ,
  previous_balance DECIMAL(14, 2)    ,
  debit DECIMAL(14, 2)    ,
  credit DECIMAL(14, 2)    ,
  current_balance DECIMAL(14, 2)    ,
  no_current_balance DECIMAL(14, 2)      ,
PRIMARY KEY(id)  ,
  FOREIGN KEY(accountant_puc_id)
    REFERENCES accountant_puc(id));


CREATE INDEX f1_format_FKIndex1 ON f1_format (accountant_puc_id);


CREATE INDEX IFK_Tiene ON f1_format (accountant_puc_id);


CREATE TABLE changes_revenue_period (
  id CHAR   NOT NULL ,
  revenue_budget_id CHAR   NOT NULL ,
  addition DECIMAL(14, 2)   NOT NULL ,
  reduction DECIMAL(14, 2)   NOT NULL ,
  credit_transfer DECIMAL(14, 2)   NOT NULL ,
  countercredit_transfer DECIMAL(14, 2)   NOT NULL ,
  created_at DATETIME   NOT NULL ,
  updated_at DATETIME   NOT NULL   ,
PRIMARY KEY(id)  ,
  FOREIGN KEY(revenue_budget_id)
    REFERENCES revenue_budget(id));


CREATE INDEX changes_revenue_period_FKIndex1 ON changes_revenue_period (revenue_budget_id);


CREATE INDEX IFK_Tiene ON changes_revenue_period (revenue_budget_id);


CREATE TABLE expenses_budget (
  id CHAR   NOT NULL ,
  budget_item_expenses_id CHAR   NOT NULL ,
  period VARCHAR(20)   NOT NULL ,
  initial_appropriation DECIMAL(14, 2)   NOT NULL ,
  final_appropriation DECIMAL(14, 2)   NOT NULL ,
  created_at DATETIME   NOT NULL ,
  updated_at DATETIME   NOT NULL   ,
PRIMARY KEY(id)  ,
  FOREIGN KEY(budget_item_expenses_id)
    REFERENCES budget_item_expenses(id));


CREATE INDEX expenses_budget_FKIndex1 ON expenses_budget (budget_item_expenses_id);


CREATE INDEX IFK_Tiene ON expenses_budget (budget_item_expenses_id);


CREATE TABLE cumulative_changes_revenue (
  id CHAR   NOT NULL ,
  revenue_budget_id CHAR   NOT NULL ,
  accumulated_additions DECIMAL(14, 2)   NOT NULL ,
  accumulated_reductions DECIMAL(14,2)   NOT NULL ,
  transfer_accumulated_credits DECIMAL(14, 2)   NOT NULL ,
  transfer_accumulated_countercredits DECIMAL(14, 2)   NOT NULL ,
  created_at DATETIME   NOT NULL ,
  updated_at DATETIME   NOT NULL   ,
PRIMARY KEY(id)  ,
  FOREIGN KEY(revenue_budget_id)
    REFERENCES revenue_budget(id));


CREATE INDEX cumulative_changes_revenue_FKIndex1 ON cumulative_changes_revenue (revenue_budget_id);


CREATE INDEX IFK_Tiene ON cumulative_changes_revenue (revenue_budget_id);


CREATE TABLE f11_accounts_payable (
  id CHAR   NOT NULL ,
  budget_item_expenses_id CHAR   NOT NULL ,
  institutions_id_institution CHAR   NOT NULL ,
  description VARCHAR(20)   NOT NULL ,
  account_payable DECIMAL(14, 2)   NOT NULL ,
  cancellation_certificate DECIMAL(14, 2)   NOT NULL ,
  payment DECIMAL(14, 2)   NOT NULL ,
  created_at DATETIME   NOT NULL ,
  update_at DATETIME   NOT NULL   ,
PRIMARY KEY(id)    ,
  FOREIGN KEY(institutions_id_institution)
    REFERENCES institutions(id_institution),
  FOREIGN KEY(budget_item_expenses_id)
    REFERENCES budget_item_expenses(id));


CREATE INDEX f11_accounts_payable_FKIndex1 ON f11_accounts_payable (institutions_id_institution);
CREATE INDEX f11_accounts_payable_FKIndex2 ON f11_accounts_payable (budget_item_expenses_id);


CREATE INDEX IFK_Tiene ON f11_accounts_payable (institutions_id_institution);
CREATE INDEX IFK_Tiene ON f11_accounts_payable (budget_item_expenses_id);


CREATE TABLE f7_budget_execution_expenses (
  id CHAR   NOT NULL ,
  institutions_id_institution CHAR   NOT NULL ,
  budget_item_expenses_id CHAR   NOT NULL ,
  expense_accounts_id  CHAR   NOT NULL ,
  initial_appropriation DECIMAL(14, 2)   NOT NULL ,
  credit DECIMAL(14, 2)   NOT NULL ,
  countercredit DECIMAL(14, 2)   NOT NULL ,
  postponement DECIMAL(14, 2)   NOT NULL ,
  displacement DECIMAL(14, 2)   NOT NULL ,
  reductions DECIMAL(14, 2)   NOT NULL ,
  additions DECIMAL(14, 2)   NOT NULL ,
  commitment_budget_registration DECIMAL(14, 2)   NOT NULL ,
  obligations_payments DECIMAL(14, 2)   NOT NULL ,
  created_at DATETIME   NOT NULL ,
  updated_at DATETIME   NOT NULL   ,
PRIMARY KEY(id)      ,
  FOREIGN KEY(expense_accounts_id )
    REFERENCES expense_accounts(id ),
  FOREIGN KEY(budget_item_expenses_id)
    REFERENCES budget_item_expenses(id),
  FOREIGN KEY(institutions_id_institution)
    REFERENCES institutions(id_institution));


CREATE INDEX f7_budget_execution_expenses_FKIndex1 ON f7_budget_execution_expenses (expense_accounts_id );
CREATE INDEX f7_budget_execution_expenses_FKIndex2 ON f7_budget_execution_expenses (budget_item_expenses_id);
CREATE INDEX f7_budget_execution_expenses_FKIndex3 ON f7_budget_execution_expenses (institutions_id_institution);


CREATE INDEX IFK_Tiene ON f7_budget_execution_expenses (expense_accounts_id );
CREATE INDEX IFK_Tiene ON f7_budget_execution_expenses (budget_item_expenses_id);
CREATE INDEX IFK_Tiene ON f7_budget_execution_expenses (institutions_id_institution);


CREATE TABLE payment_relationship (
  id CHAR   NOT NULL ,
  institutions_id_institution CHAR   NOT NULL ,
  bank_id  CHAR   NOT NULL ,
  budget_item_expenses_id CHAR   NOT NULL ,
  date DATE   NOT NULL ,
  no_exit_receipt CHAR(5)   NOT NULL ,
  accounting_account CHAR(5)   NOT NULL ,
  contract_number CHAR(10)   NOT NULL ,
  invoice_number CHAR(10)   NOT NULL ,
  beneficiary_payment VARCHAR(20)   NOT NULL ,
  cc_nit CHAR(20)   NOT NULL ,
  datail VARCHAR(50)   NOT NULL ,
  invoice_value DECIMAL(14, 2)   NOT NULL ,
  rte_fte DECIMAL(14, 2)    ,
  reteiva DECIMAL(14, 2)    ,
  other_discounts DECIMAL(14, 2)    ,
  net_value DECIMAL(14, 2)   NOT NULL ,
  check_number CHAR(5)   NOT NULL ,
  source_funding VARCHAR(20)   NOT NULL ,
  benefited VARCHAR(20)   NOT NULL ,
  created_at DATETIME   NOT NULL ,
  update_at DATETIME   NOT NULL   ,
PRIMARY KEY(id)      ,
  FOREIGN KEY(budget_item_expenses_id)
    REFERENCES budget_item_expenses(id),
  FOREIGN KEY(bank_id )
    REFERENCES bank(id ),
  FOREIGN KEY(institutions_id_institution)
    REFERENCES institutions(id_institution));


CREATE INDEX payment_relationship_FKIndex1 ON payment_relationship (budget_item_expenses_id);
CREATE INDEX payment_relationship_FKIndex2 ON payment_relationship (bank_id );
CREATE INDEX payment_relationship_FKIndex3 ON payment_relationship (institutions_id_institution);


CREATE INDEX IFK_Tiene ON payment_relationship (budget_item_expenses_id);
CREATE INDEX IFK_Tiene ON payment_relationship (bank_id );
CREATE INDEX IFK_Tiene ON payment_relationship (institutions_id_institution);


CREATE TABLE ief04_payments_relationship (
  id CHAR   NOT NULL ,
  institutions_id_institution CHAR   NOT NULL ,
  source_resoureces_id CHAR   NOT NULL ,
  bank_id  CHAR   NOT NULL ,
  budget_item_expenses_id CHAR   NOT NULL ,
  collection_date DATE   NOT NULL ,
  receipt_number CHAR(10)   NOT NULL ,
  detail VARCHAR(20)   NOT NULL ,
  beneficiary VARCHAR(10)   NOT NULL ,
  cc_nit CHAR(10)   NOT NULL ,
  total_value_receipt DECIMAL(14, 2)   NOT NULL ,
  withholdings DECIMAL(14, 2)   NOT NULL ,
  discounts DECIMAL(14, 2)   NOT NULL ,
  account_number CHAR(10)   NOT NULL ,
  check_number CHAR(10)   NOT NULL ,
  created_at DATETIME   NOT NULL ,
  updated_at DATETIME   NOT NULL   ,
PRIMARY KEY(id)        ,
  FOREIGN KEY(budget_item_expenses_id)
    REFERENCES budget_item_expenses(id),
  FOREIGN KEY(bank_id )
    REFERENCES bank(id ),
  FOREIGN KEY(source_resoureces_id)
    REFERENCES source_resoureces(id),
  FOREIGN KEY(institutions_id_institution)
    REFERENCES institutions(id_institution));


CREATE INDEX ief04_payments_relationship_FKIndex1 ON ief04_payments_relationship (budget_item_expenses_id);
CREATE INDEX ief04_payments_relationship_FKIndex2 ON ief04_payments_relationship (bank_id );
CREATE INDEX ief04_payments_relationship_FKIndex3 ON ief04_payments_relationship (source_resoureces_id);
CREATE INDEX ief04_payments_relationship_FKIndex4 ON ief04_payments_relationship (institutions_id_institution);


CREATE INDEX IFK_Tiene ON ief04_payments_relationship (budget_item_expenses_id);
CREATE INDEX IFK_Tiene ON ief04_payments_relationship (bank_id );
CREATE INDEX IFK_Tiene ON ief04_payments_relationship (source_resoureces_id);
CREATE INDEX IFK_Tiene ON ief04_payments_relationship (institutions_id_institution);


CREATE TABLE f13_hiring (
  id CHAR   NOT NULL ,
  institutions_id_institution CHAR   NOT NULL ,
  expense_accounts_id  CHAR   NOT NULL ,
  source_resoureces_id CHAR   NOT NULL ,
  budget_item_expenses_id CHAR   NOT NULL ,
  contract_number CHAR(10)   NOT NULL ,
  object VARCHAR(20)   NOT NULL ,
  contract_value DECIMAL(14, 2)   NOT NULL ,
  contractor_name VARCHAR(20)   NOT NULL ,
  nit_cc_contractor CHAR(10)   NOT NULL ,
  budget_unavailability DECIMAL(14, 2)   NOT NULL ,
  value_availability DECIMAL(14, 2)   NOT NULL ,
  signature_date DATE   NOT NULL ,
  contract_form CHAR(5)   NOT NULL ,
  budget_registration_number_3 DATE   NOT NULL ,
  budget_registration_number CHAR(10)   NOT NULL ,
  budget_record_value DECIMAL(14, 2)   NOT NULL ,
  date_approval_single_guarantee DATE    ,
  start_date DATE   NOT NULL ,
  contract_term VARCHAR(50)   NOT NULL ,
  addition_date DATE    ,
  addition_term DATE    ,
  addition_value DECIMAL(14, 2)   NOT NULL ,
  value_payments_made DECIMAL(14, 2)   NOT NULL ,
  completion_date DATE   NOT NULL ,
  settlement_date DATE   NOT NULL ,
  created_at DATETIME   NOT NULL ,
  updated_at DATETIME   NOT NULL   ,
PRIMARY KEY(id)        ,
  FOREIGN KEY(budget_item_expenses_id)
    REFERENCES budget_item_expenses(id),
  FOREIGN KEY(source_resoureces_id)
    REFERENCES source_resoureces(id),
  FOREIGN KEY(expense_accounts_id )
    REFERENCES expense_accounts(id ),
  FOREIGN KEY(institutions_id_institution)
    REFERENCES institutions(id_institution));


CREATE INDEX f13_hiring_FKIndex1 ON f13_hiring (budget_item_expenses_id);
CREATE INDEX f13_hiring_FKIndex2 ON f13_hiring (source_resoureces_id);
CREATE INDEX f13_hiring_FKIndex3 ON f13_hiring (expense_accounts_id );
CREATE INDEX f13_hiring_FKIndex4 ON f13_hiring (institutions_id_institution);


CREATE INDEX IFK_Tiene ON f13_hiring (budget_item_expenses_id);
CREATE INDEX IFK_Tiene ON f13_hiring (source_resoureces_id);
CREATE INDEX IFK_Tiene ON f13_hiring (expense_accounts_id );
CREATE INDEX IFK_Tiene ON f13_hiring (institutions_id_institution);


CREATE TABLE ief02_revenue_statement (
  id CHAR   NOT NULL ,
  bank_id  CHAR   NOT NULL ,
  source_resoureces_id CHAR   NOT NULL ,
  budget_item_revenue_id CHAR   NOT NULL ,
  institutions_id_institution CHAR   NOT NULL ,
  collection_date DATE   NOT NULL ,
  detail VARCHAR(20)   NOT NULL ,
  value DECIMAL(14, 2)   NOT NULL ,
  bank_account_number CHAR(10)   NOT NULL ,
  bank VARCHAR(20)   NOT NULL ,
  created_at DATETIME   NOT NULL ,
  updatetd_at DATETIME   NOT NULL   ,
PRIMARY KEY(id)        ,
  FOREIGN KEY(institutions_id_institution)
    REFERENCES institutions(id_institution),
  FOREIGN KEY(budget_item_revenue_id)
    REFERENCES budget_item_revenue(id),
  FOREIGN KEY(source_resoureces_id)
    REFERENCES source_resoureces(id),
  FOREIGN KEY(bank_id )
    REFERENCES bank(id ));


CREATE INDEX ief02_revenue_statement_FKIndex1 ON ief02_revenue_statement (institutions_id_institution);
CREATE INDEX ief02_revenue_statement_FKIndex2 ON ief02_revenue_statement (budget_item_revenue_id);
CREATE INDEX ief02_revenue_statement_FKIndex3 ON ief02_revenue_statement (source_resoureces_id);
CREATE INDEX ief02_revenue_statement_FKIndex4 ON ief02_revenue_statement (bank_id );


CREATE INDEX IFK_Tiene ON ief02_revenue_statement (institutions_id_institution);
CREATE INDEX IFK_Tiene ON ief02_revenue_statement (budget_item_revenue_id);
CREATE INDEX IFK_Tiene ON ief02_revenue_statement (source_resoureces_id);
CREATE INDEX IFK_Tiene ON ief02_revenue_statement (bank_id );


CREATE TABLE revenue_execution (
  id CHAR   NOT NULL ,
  revenue_budget_id CHAR   NOT NULL ,
  montly_revenue_value DECIMAL(14, 2)   NOT NULL ,
  accumulated_revenue DECIMAL(14, 2)   NOT NULL ,
  revenue_receivable DECIMAL(14, 2)   NOT NULL ,
  created_at DATETIME   NOT NULL ,
  updated_at DATETIME   NOT NULL   ,
PRIMARY KEY(id)  ,
  FOREIGN KEY(revenue_budget_id)
    REFERENCES revenue_budget(id));


CREATE INDEX revenue_execution_FKIndex1 ON revenue_execution (revenue_budget_id);


CREATE INDEX IFK_Tiene ON revenue_execution (revenue_budget_id);


CREATE TABLE payment_obligations (
  id CHAR   NOT NULL ,
  expenses_budget_id CHAR   NOT NULL ,
  open_positions DECIMAL(14, 2)   NOT NULL ,
  obligations_period DECIMAL(14, 2)   NOT NULL ,
  accumulated_obligations DECIMAL(14, 2)   NOT NULL ,
  period_payments DECIMAL(14, 2)   NOT NULL ,
  accumulated_payments DECIMAL(14, 2)   NOT NULL ,
  balance_payable DECIMAL(14, 2)   NOT NULL ,
  reservations DECIMAL(14, 2)   NOT NULL ,
  created_at DATETIME   NOT NULL ,
  updated_at DATETIME   NOT NULL   ,
PRIMARY KEY(id)  ,
  FOREIGN KEY(expenses_budget_id)
    REFERENCES expenses_budget(id));


CREATE INDEX payment_obligations_FKIndex1 ON payment_obligations (expenses_budget_id);


CREATE INDEX IFK_Tiene ON payment_obligations (expenses_budget_id);


CREATE TABLE cumulative_changes_expenses (
  id CHAR   NOT NULL ,
  expenses_budget_id CHAR   NOT NULL ,
  accumulated_additions DECIMAL(14, 2)   NOT NULL ,
  accumulated_reductions DECIMAL(14, 2)   NOT NULL ,
  accumulated_credits DECIMAL(14, 2)   NOT NULL ,
  accumulated_countercredist DECIMAL(14, 2)   NOT NULL ,
  created_at DATETIME   NOT NULL ,
  updated_at DATETIME   NOT NULL   ,
PRIMARY KEY(id)  ,
  FOREIGN KEY(expenses_budget_id)
    REFERENCES expenses_budget(id));


CREATE INDEX cumulative_changes_expenses_FKIndex1 ON cumulative_changes_expenses (expenses_budget_id);


CREATE INDEX IFK_Tiene ON cumulative_changes_expenses (expenses_budget_id);


CREATE TABLE changes_epenses_period (
  id CHAR   NOT NULL ,
  expenses_budget_id CHAR   NOT NULL ,
  addition DECIMAL(14, 2)   NOT NULL ,
  reduction DECIMAL(14, 2)   NOT NULL ,
  credits DECIMAL(14, 2)   NOT NULL ,
  countercredits DECIMAL(14, 2)   NOT NULL ,
  created_at DATETIME   NOT NULL ,
  updated_at DATETIME   NOT NULL   ,
PRIMARY KEY(id)  ,
  FOREIGN KEY(expenses_budget_id)
    REFERENCES expenses_budget(id));


CREATE INDEX changes_epenses_period_FKIndex1 ON changes_epenses_period (expenses_budget_id);


CREATE INDEX IFK_Tiene ON changes_epenses_period (expenses_budget_id);


CREATE TABLE expenses_execution (
  id CHAR   NOT NULL ,
  expenses_budget_id CHAR   NOT NULL ,
  certificates_perios DECIMAL(14, 2)   NOT NULL ,
  accumulated_certificates DECIMAL(14, 2)   NOT NULL ,
  available_balance DECIMAL(14, 2)   NOT NULL ,
  period_commitments DECIMAL(14, 2)   NOT NULL ,
  accumulated_commitments DECIMAL(14, 2)   NOT NULL ,
  created_at DATETIME   NOT NULL ,
  updated_at DATETIME   NOT NULL   ,
PRIMARY KEY(id)  ,
  FOREIGN KEY(expenses_budget_id)
    REFERENCES expenses_budget(id));


CREATE INDEX expenses_execution_FKIndex1 ON expenses_execution (expenses_budget_id);


CREATE INDEX IFK_Tiene ON expenses_execution (expenses_budget_id);
