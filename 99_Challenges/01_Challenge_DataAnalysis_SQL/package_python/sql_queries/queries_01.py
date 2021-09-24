q_task1 = '''
            select
                O.merchant_uuid as merchant_id,
                count(O.uuid) as num_creditos,
                round(sum(O.booking)::numeric, 2) as Sales
            from public.orders as O
            inner join public.merchants as M
            on O.merchant_uuid = M.uuid
            where O.number_instalments > 0 and O.annual_percentage_rate > 0
            group by merchant_id
            order by  num_creditos desc
            '''