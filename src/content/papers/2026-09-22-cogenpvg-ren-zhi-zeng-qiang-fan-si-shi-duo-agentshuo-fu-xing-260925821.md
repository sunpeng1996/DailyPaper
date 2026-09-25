---
title: 'CogenPVG: Cognitive-Enhanced Reflective Multi-Agent Framework for Persuasive
  Video Generation'
title_zh: CogenPVG：认知增强反思式多Agent说服性视频生成框架
authors:
- Yuntian Xiao
- Shoulong Zhang
- Wenfeng Song
- Yan Wang
- Yi Chen
- Shuai Li
affiliations:
- Beihang University
- Zhongguancun Laboratory
- Beijing Information Science and Technology University
- Beijing Technology and Business University
arxiv_id: '2609.25821'
url: https://arxiv.org/abs/2609.25821
pdf_url: https://arxiv.org/pdf/2609.25821
published: '2026-09-22'
collected: '2026-09-25'
category: MultiAgent
direction: 多智体协作 · 说服性视频生成
tags:
- MultiAgent
- PersuasiveContent
- VideoGeneration
- ELM
- LLM4Multimodal
one_liner: 基于ELM心理学理论设计四阶段生成-批评多Agent框架，实现高说服力通用主题视频生成
practical_value: '- 电商带货/种草短视频生成可直接复用四阶段生成-批评反思架构，搭配ELM双路径原则：理性层接入商品参数、权威检测报告等数据源做论证，感性层优化视听情绪唤起，直接提升内容转化率

  - Agent协作流程可复用「分阶段专业化+每阶段生成-批评迭代」的设计，每个环节锚定可量化的业务标准（如可信度、情绪匹配度），避免端到端生成的黑盒不可控问题

  - 内容效果评估可复用LMM+人工结合的双维度体系，引入平均态度偏移(AAS)等指标衡量内容对用户决策的实际影响，替代传统仅看内容质感的评估逻辑

  - 若需降低生成成本，可根据业务场景裁剪反射迭代次数，优先保证中央路径论证的可信度，再逐步优化外围路径的视听体验，兼顾效果与效率'
score: 8
source: arxiv-cs.MM
depth: full_pdf
---

### 动机
现有多Agent视频生成方案仅聚焦叙事性内容的视觉一致性，完全忽略对用户态度的引导能力；而短视频平台带货、品牌宣传、科普等场景对高说服力内容需求极强，说服性视频生成（PVG）领域长期缺乏可落地的通用框架，传统方案无法平衡理性论证可信度与感性情绪感染力的协同效果。

### 方法关键点
- 基于心理学ELM精细加工可能性模型设计双路径增强逻辑：中央路径聚焦论证的逻辑严谨性与可信度，匹配用户深度思考场景；外围路径通过视听设计降低认知负荷、唤起情绪共鸣，匹配用户浅层感知场景
- 拆解视频生成全流程为4个串行阶段：论证推理、分镜规划、资产生成、后期剪辑，每个阶段配对生成Agent+批评Agent，基于对应心理学标准迭代优化输出，避免单Agent能力短板
- 论证推理阶段接入网页搜索工具获取权威证据，用Paul-Elder批判性思维模型校验论证的相关性、深度、精度等8项指标；其余三个阶段基于流畅性启发、情绪启发等原则优化视听体验

### 关键实验
基于PVP数据集构造72组通用主题+立场的测试样本，对比MM-StoryAgent、Anim-Director、商用VideoGen等5个基线：人类评估下CogenPVG的平均态度偏移(AAS)达0.604，较最优基线DirectPVG提升74%；对初始持反对/中立态度的用户态度提升分别达3.268/2.296，人类说服力高分段占比较消去双路径的版本提升14.8%。

**最值得记住的结论：** 说服性内容的效果取决于理性论证与感性唤起的协同平衡，仅强化单一路径反而会触发认知干扰，降低整体说服力。
