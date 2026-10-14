---
title: Choosing LLMs for Strategic Agent Interactions
title_zh: 面向智能体策略交互场景的大语言模型选型方法研究
authors:
- Arastun Mammadli
- Herbert Woisetschläger
- Jawad Fayaz
- Shiqiang Wang
affiliations:
- University of Exeter
- IBM Research
arxiv_id: '2610.18354'
url: https://arxiv.org/abs/2610.18354
pdf_url: https://arxiv.org/pdf/2610.18354
published: '2026-10-13'
collected: '2026-10-14'
category: Agent
direction: 智能体策略交互 · LLM选型路由
tags:
- LLM Routing
- Multi-Agent
- Game Theory
- Thompson Sampling
- Strategic Reasoning
one_liner: 将LLM路由转化为策略元博弈问题，对比7种选型方法在5类博弈场景的表现
practical_value: '- 做电商竞价、议价、谈判类Agent时，不要盲目选大模型，可先基于业务场景预跑小范围配对测试，筛选性价比最高的小模型栈，比如论文中3B的Granite在Vickrey拍卖场景性能超过24B-70B模型，可大幅降本

  - 动态对手场景下的LLM路由优先选用轻量Thompson Sampling实现，效果优于基于query embedding的路由、LLM自反射路由，甚至非平稳/对抗bandit变种也不如基础TS，可省掉复杂的路由模型开发成本

  - 做Agent策略效果评测时，要根据场景信噪比设置足够的重复实验次数，博弈类交互场景需要至少150次种子跑才能得到统计显著的结果，避免少量实验的结论偏差

  - 可借鉴论文的策略倾向（disposition）建模方法，给业务LLM打行为标签（如冒险、合作倾向），针对不同对手匹配对应倾向的模型，优化长期收益'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有LLM路由仅基于静态任务分布做性能-成本权衡，未考虑多智能体交互中对手动态自适应的特性；而博弈论方向的LLM策略评测仅固定单模型测试，未利用不同模型在不同场景、不同对手下的性能差异做动态选型，无法应对真实交互中对手策略变化的非平稳环境。

### 方法关键点
- 提出双层元博弈框架：底层是选出的LLM与对手进行博弈，上层是选型器作为元博弈玩家，每轮从模型栈中选出最优LLM参战，基于历史对局反馈更新选型策略
- 对比7种选型方法：包括基于embedding的路由（RouterDC、Causal LLM Router）、LLM自反射路由、Thompson Sampling（TS）及其非平稳变种（滑动窗口TS、折扣TS）、对抗bandit EXP3
- 设计博弈场景信噪比评测方法，量化不同场景所需的种子实验次数，保证结论统计显著

### 关键实验
覆盖10款3B-70B开源LLM（Granite、Mistral、Llama、Qwen），在5类经典博弈场景（Colonel Blotto、古诺双寡头、猎鹿博弈、维克里拍卖、胆小鬼博弈）测试：1）模型大小与策略能力相关性仅0.37，考虑成本后相关性为-0.54，小模型在特定场景性能显著优于大模型；2）基础TS在所有场景的净收益均最优，比embedding路由高5%-16%，比LLM自反射路由高24%-39%，但仍低于最优固定模型的性能上限；3）非平稳/对抗bandit变种效果不如基础TS，说明当前方法无法有效捕获对手策略变化的信号。

### 最值得记住的一句话
策略交互场景下的LLM选型，场景适配性比模型大小重要，轻量在线反馈的bandit方法比复杂的语义路由或LLM自反射方案更可靠。
