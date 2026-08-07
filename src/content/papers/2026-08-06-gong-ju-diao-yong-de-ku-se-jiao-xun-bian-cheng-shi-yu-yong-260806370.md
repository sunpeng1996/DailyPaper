---
title: The Bitter Lesson of Tool Calling
title_zh: 工具调用的苦涩教训：编程式与JSON调用的跨模型对比评测
authors:
- Ishan Patel
- Sahil Sen
- Elias Lumer
- Vamse Kumar Subbiah
affiliations:
- PricewaterhouseCoopers (PwC), U.S.A
arxiv_id: '2608.06370'
url: https://arxiv.org/abs/2608.06370
pdf_url: https://arxiv.org/pdf/2608.06370
published: '2026-08-06'
collected: '2026-08-07'
category: Agent
direction: Agent工具调用范式优化
tags:
- Tool Calling
- LLM Agent
- Programmatic Tool Calling
- JSON Tool Calling
- Benchmark
one_liner: 基于BFCL v4基准对比14款LLM的两种工具调用范式，验证编程式调用的鲁棒优势与适用边界
practical_value: '- 若业务使用Claude全系列、GPT-5.6及以上新模型，可直接将JSON工具调用替换为Python编程式调用，长链任务可降低约50%延迟，最高提升10.6%的调用准确率

  - 高并行多工具调用场景（如电商Agent同时拉取商品库存、价格、优惠、物流信息）优先使用编程式调用，支持N=100并行调用无性能下降，且N≥26时token消耗低于JSON调用

  - 上下文存在大量冗余工具定义的场景（如Agent内置数十上百个运营、商品、用户相关工具），编程式调用比JSON更稳定，平均无精度下降甚至有5.5%的提升

  - 若使用GPT-4o、GPT-4.1、GPT-5.4-mini等旧OpenAI模型，暂不要切换编程式调用，会因换行符编码错误导致最多26.9%的准确率下降'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前LLM Agent主流采用JSON格式调用工具，但编程式调用（通过Python脚本调用工具）理论上更适配具备代码生成能力的模型，却缺乏跨多代模型、真实任务场景下的系统性评测，两种范式的优劣势和适用边界尚未明确。
### 方法关键点
- 评测设计：对比JSON原生工具调用（模型输出结构化JSON对象触发工具调用）和编程式工具调用（给模型提供对应工具的Python类型存根，模型编写调用脚本，Agent单轮执行脚本获取结果），两种范式消耗相同LLM调用次数，保证对比公平
- 数据集：基于BFCL v4基准的309条样本，覆盖8类任务（单调用、多调用、并行调用、真实用户场景等），额外设置三类消融场景：链长2~20的串行调用、扇出数7~100的并行调用、注入128个冗余工具的上下文腐蚀场景
- 评测对象：覆盖2024年11月到2026年7月发布的14款Anthropic、OpenAI模型，温度设为0，采用确定性规则评分
### 关键结果
11/14的模型上编程式调用准确率持平或超过JSON调用，GPT-5.6系列最高提升10.6%；旧OpenAI模型（GPT-4o、GPT-4.1、GPT-5.4-mini）因换行符编码错误，准确率最多下降26.9%。长链任务（链长≥12）编程式调用领先JSON 18.8%，延迟降低约50%；并行调用场景JSON在N≥72（Claude Sonnet 5）时开始丢失调用，编程式在N=100时仍保持100%准确率，N≥26时token消耗更低；上下文腐蚀场景JSON平均掉点2.3%，编程式平均提升5.5%。
> 最值得记住的结论：编程式工具调用的适配性仅和模型生成合格Python代码的能力相关，与模型家族无关，新模型可优先切换。
