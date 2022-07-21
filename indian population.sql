   
   select * from project.dbo.Data1
select * from project.dbo.Sheet1
select count(*) from project..Data1
select count(*) from project..Sheet1

-- generate data for jharkhand and maharashtra

select * from project..Data1 where state in ('Jharkhand','Maharashtra')

-- population of India

select sum(population)as Population from project..Sheet1

-- average growth of India

select AVG(Growth) * 100  as Average_growth from PROJECT..Data1

-- average growth per state


select state ,AVG(Growth) * 100  as Average_growth_percentage from PROJECT..Data1 group by state

-- average sex ratio per state

select state ,round(AVG(Sex_Ratio),2) as Average_Sex_Ratio from PROJECT..Data1 group by state order by Average_Sex_Ratio desc

--average literacy rate

select state ,round(AVG(Literacy),2) as Literacy from PROJECT..Data1 group by state order by Literacy desc

select state ,round(AVG(Literacy),2) as Literacy from PROJECT..Data1 group by state having round(AVG(Literacy),2)>80 order by Literacy asc

--top 3 state showing highest growth ratio

select top 3 state ,round(AVG(Literacy),2) as Literacy from PROJECT..Data1 group by state having round(AVG(Literacy),2)>80 order by Literacy desc

select top 3 state, round(avg(Sex_Ratio),0) avg_Sex_Ratio from project..Data1 group by state order by avg_Sex_Ratio asc


--states starting "A"

select * from project..Sheet1 where lower(state) like 'a%' or lower(state) like 'J%'

'