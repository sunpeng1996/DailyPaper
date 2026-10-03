---
title: Who Thinks First? Designing Productive Friction with Engage-to-Unlock GenAI
title_zh: 先思考再用AI：为生成式AI设计「参与解锁」型生产性摩擦机制
authors:
- Xiaotian Su
- Laura Rimell
- Jiazheng Li
- Amal Rannen-Triki
- Ulrich Paquet
- Lisa Anne Hendricks
- Rida Qadri
- Daphne Ippolito
- Piotr Mirowski
affiliations:
- Google DeepMind
- ETH Zurich
- King's College London
- Google Research
arxiv_id: '2610.01518'
url: https://arxiv.org/abs/2610.01518
pdf_url: https://arxiv.org/pdf/2610.01518
published: '2026-10-01'
collected: '2026-10-03'
category: LLM
direction: 人机协作 · GenAI访问机制设计
tags:
- Human-AI-Interaction
- Productive-Friction
- GenAI
- AI-Assisted-Writing
- Access-Control
one_liner: 提出用户先有效参与任务再解锁GenAI的生产性摩擦机制，验证其可提升人机协作效率
practical_value: '- 电商文案生成、广告素材产出场景可复用「参与解锁」机制，要求运营先输入核心卖点、目标人群等关键信息后再解锁LLM生成能力，降低认知卸载导致的生成内容脱离业务需求的概率

  - 推荐系统标注、query改写审核等流程可加入前置任务摩擦，要求标注员先输出初步判断再调用AI辅助校验，可同时提升标注效率与准确率

  - Agent工具调用链路可加入触发门槛，仅当用户输入的需求信息完整度达到阈值时才解锁RAG/检索等工具调用，减少无效工具调用的开销'
score: 7
source: arxiv-cs.HC
depth: abstract
---

### 动机
当前GenAI无摩擦访问易使用户在形成独立思路前发生认知卸载，既降低用户对任务的掌控度，也容易导致AI输出脱离实际需求，现有机制未平衡AI赋能与用户主动思考的关系。
### 方法关键点
提出Engage-to-Unlock生产性摩擦机制，仅当用户对目标任务完成有效参与后才解锁GenAI生成能力；设置四组对照实验：纯人工、标准无限制Chatbot、参与解锁、时间匹配解锁（仅对齐解锁时间不关联用户参与度），共398名参与者完成写作+文本校验任务。
### 关键结果数字
1. 参与解锁组未增加总任务时长，同时实现任务精力再分配：自主写作时间占比提升、后续校验时间占比降低
2. 较其他AI辅助组提交prompt数量更多，单位时间评估准确率为所有组别最高
