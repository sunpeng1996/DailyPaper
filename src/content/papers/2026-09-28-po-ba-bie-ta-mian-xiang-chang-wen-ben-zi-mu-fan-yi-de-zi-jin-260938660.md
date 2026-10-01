---
title: 'Breaking Babel: A Self-Evolving Multi-Agent System for Long-Form Subtitle
  Translation'
title_zh: 破巴别塔：面向长文本字幕翻译的自进化多智能体系统
authors:
- Haibo Jin
- Xinjie Li
- Najmeh Sadoughi
- Yang Liu
- Yibo Wang
- Zhu Liu
- Yuzong Liu
affiliations:
- University of Illinois Urbana-Champaign
- Amazon
arxiv_id: '2609.38660'
url: https://arxiv.org/abs/2609.38660
pdf_url: https://arxiv.org/pdf/2609.38660
published: '2026-09-28'
collected: '2026-10-01'
category: Agent
direction: 多Agent · 自进化长文本任务处理
tags:
- Multi-Agent
- Self-Evolving
- Test-Time Training
- MoA
- LLM Translation
one_liner: 提出无需微调LLM的自进化多Agent长字幕翻译框架SMART及配套评测体系
practical_value: '- 自进化多Agent架构可直接复用在电商跨境场景的多语言文案生成、商品详情页翻译、评价多语言对齐任务，无需微调LLM，仅通过test-time训练优化prompt和路由策略即可适配业务，大幅降低迭代成本

  - 分层持久化记忆池（术语库/角色库/领域知识库/习语库）的设计可迁移到推荐系统的用户/物品长期兴趣建模、Agent对话上下文一致性维护，解决长序列下的信息遗忘与一致性漂移问题

  - 动态路由+MoA的调度逻辑可复用在搜索推荐多模型融合排序场景，根据query/物品特征动态选择最优模型子集，在降低推理成本的同时提升效果

  - 文本反馈驱动的prompt与路由优化方法，可替代传统RLHF用于生成式推荐的文案效果调优，基于业务评价反馈自动迭代prompt，无需标注大量训练数据'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
长字幕翻译难度远高于常规机器翻译：单集可能包含数百个依赖长程上下文、文化背景的句子，还要保证跨剧集术语、叙事风格的一致性，同时满足字幕时长、长度等展示约束。现有单LLM方法缺乏长上下文感知能力，术语易漂移；多Agent方法多采用固定工作流，无法适配不同场景的复杂度差异，且均忽略体裁、时代背景等生产上下文信息，效果受限。

### 方法关键点
- 两阶段工作流：test-time训练阶段用30%剧集数据迭代优化Agent prompt、路由策略，构建系列级持久化记忆；推理阶段冻结配置翻译剩余70%内容，记忆持续更新
- 核心模块：动态图路由根据句子特征（长度、风格、俚语等）选择匹配的翻译专家（忠实/自然/表达/长度感知/口语化共5类）；MoA翻译层生成多候选结果，配套术语校验、字幕约束验证、上下文检索等工具链；裁判-精炼回路打分候选并输出文本反馈，反向优化prompt和路由，全程不更新底层LLM参数
- 配套评测：构建Subtitle Arena基准，覆盖14类体裁、15个目标语种、192部剧集；提出SubMQM多维度字幕评测指标，含7个维度19类错误

### 关键结果
- 在Subtitle Arena 15个翻译方向上均取得最优SubMQM得分，比最强Agent基线TransAgent平均罚分降低6.9%，人工评价得分4.50/5位列第一
- 公开基准MuSC上4个语言对全部取得最优结果，比最强基线平均提升3.0个点，生动性维度最高提升7.9个点
- 消融实验显示持久化记忆贡献最大，移除后平均罚分升高0.78，其次是MoA（+0.61）、上下文检索（+0.56）

最值得记住的一句话：长文本复杂任务的处理不需要依赖单模型能力提升，通过自进化多Agent架构、分层记忆、动态调度结合的方式，无需微调底层LLM即可实现显著效果提升
