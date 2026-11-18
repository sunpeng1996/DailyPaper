---
title: 'What MoE Routing Controls: Causal Interventions on Expert Trajectories'
title_zh: MoE路由的控制作用：针对专家路径的因果干预研究
authors:
- Mukund Athmaram
- Manoj Rao
- Liang Ma
affiliations:
- Advanced Micro Devices Inc. (AMD)
- Cornell University
arxiv_id: '2611.22120'
url: https://arxiv.org/abs/2611.22120
pdf_url: https://arxiv.org/pdf/2611.22120
published: '2026-11-17'
collected: '2026-11-18'
category: LLM
direction: MoE大模型 · 路由路径因果干预
tags:
- MoE
- Routing
- Causal Intervention
- Model Steering
- Expert Trajectory
one_liner: 通过路由logit偏置引导MoE token走指定跨层专家路径，验证格式与概念路径的不同干预效果
practical_value: '- 对用MoE LLM做生成式推荐/营销文案生成的场景，可通过引导格式类专家路径，快速强制输出固定结构（如商品参数JSON、标准化话术），无需微调

  - 做MoE LLM服务优化时，优先调整中间层路由逻辑，对输出的控制效率远高于前后层

  - 跨语种电商内容生成场景可复用路径迁移思路：用A语种概念样本提取的专家路径，可直接干预B语种输出的概率分布，降低跨语种对齐成本

  - MoE选型时，top-k路由宽度越大（如top-8）越容易形成独立概念路径，适合需要可控输出的业务，top-k过小的MoE可控性更差'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
MoE模型的路由逻辑长期缺乏可解释性，现有干预方法多针对单个专家或隐藏状态，无法明确跨层专家路径对输出的因果影响；同时MoE在生成式推荐、多语种客服等业务中的可控生成需求迫切，亟需低成本、无微调的输出控制手段。

### 方法关键点
- 路径构建：针对目标格式/概念，取若干样例token过模型，取每层出现频次最高的top-1专家组成跨层目标路径
- 干预方式：仅在生成时给每层目标专家的路由logit加固定偏置，不修改隐藏状态或模型参数，不影响其他专家的输入
- 评估维度：同时测试下一词概率分布偏移、生成文本的实际变化两类指标，用随机路径加同等偏置作为对照组

### 关键结果数字
- 核心测试模型为Qwen3-30B-A3B（48层、128专家、top-8路由），同时覆盖4种主流MoE架构
- 格式干预：将代码中表示类型注解的冒号引导到时间格式路径，输出数字占比提升至随机路径的44倍
- 跨语种概念干预：用中文宗教样本构建路径干预英文中性prompt，英文宗教词下一词概率提升至7倍，效果跨语言迁移无损耗
- 分层测试：仅干预中间层（16-31层）的效果是前后层的5倍以上，仅干预前4个token即可触发格式的自强化效应，输出数字占比达到全量干预的76%
- 跨架构验证：top-8路由的MoE路径独立性最强，干预效果最明显，top-4/top-6路由的模型干预效果下降甚至无效

最值得记住的一句话：MoE的格式类专家路径可通过自强化效应直接改变生成文本，概念类路径仅偏移下一词概率不会直接体现在输出中，可控干预优先选择中间层路径
