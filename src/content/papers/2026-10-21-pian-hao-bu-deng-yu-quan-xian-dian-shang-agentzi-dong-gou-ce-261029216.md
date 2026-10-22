---
title: 'Preference Is Not Permission: Personalizing the Auto-Purchase Line in Agentic
  Commerce'
title_zh: 偏好不等于权限：电商Agent自动购买决策边界的个性化建模
authors:
- Ryotaro Shimizu
- Sai HtaungKham
- Mo Fan
affiliations:
- ZOZO Research
arxiv_id: '2610.29216'
url: https://arxiv.org/abs/2610.29216
pdf_url: https://arxiv.org/pdf/2610.29216
published: '2026-10-21'
collected: '2026-10-22'
category: Agent
direction: 电商Agent · 自动购买权限个性化控制
tags:
- agentic commerce
- personalization
- authorization control
- LLM agent
- e-commerce
one_liner: 提出Agent电商自动购买边界个性化任务，少量用户标注即可超越所有Prompt+模型配置效果
practical_value: '- 上线购物Agent自动购买功能时，可先叠加独立轻量warrant校验层：用小模型单独判断商品信息是否满足用户明确需求，可将弱证据下的过度购买率降为0，且仅为全量确认策略1/4的打扰量

  - 无需投入大量成本调Prompt/换模型适配不同用户的自动购买接受度：仅需收集30-40条用户的授权标注，训练简单逻辑回归模型即可实现更精准的个性化边界控制，效果优于所有Prompt+模型组合

  - 自动购买授权决策除了商品偏好匹配度，必须额外加入证据充分度、退换货可逆性、价格相对用户阈值、稀缺性四个核心因子，不同用户对各因子敏感度差异大，边界无法跨域迁移'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前Agent电商正从推荐向执行演进，调研显示74%用户愿意委托日常购物，但仅1/10接受无确认自动购买；现有基准仅聚焦商品偏好匹配度，完全未覆盖「什么时候Agent可自主下单无需询问用户」的授权边界问题，过度决策会引发用户信任危机，过度询问又会大幅增加用户负担。

### 方法关键点
- 构造最小改动反事实基准，固定商品和用户需求，每次仅调整一个授权因子（证据充分度、可逆性、相对价格、稀缺性），覆盖服饰、酒店两个垂直领域；
- 定义三分类自动购买边界任务：不买、先确认、自动购买，收集15名标注员扮演用户的1110条授权标注作为黄金基准；
- 测试16款指令微调LLM的默认校准效果，对比Prompt调优、通用校验层、个性化小模型三种方案的边界控制效果。

### 关键结果
- 现有LLM普遍存在过度授权问题，即使商品匹配度低、自身判断证据不足时仍会自动下单，Prompt调整无法解决个体差异问题；
- 通用轻量warrant校验层可将所有模型的弱证据下过度购买率降为0，仅产生全量确认策略1/4的确认请求；
- 仅用30-40条用户个人授权标注训练的逻辑回归模型，预测用户自动购买边界的中位准确率达0.79，优于80种Prompt×模型配置的最优效果。

### 核心结论
偏好不等于权限，推荐系统判断商品匹配度高，完全不代表Agent有权限直接替用户自动下单。
