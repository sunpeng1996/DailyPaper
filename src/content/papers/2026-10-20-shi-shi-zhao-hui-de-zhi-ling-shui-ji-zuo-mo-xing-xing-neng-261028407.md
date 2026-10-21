---
title: 'The Instruction Tax on Factual Recall: Base Models Can Beat Their Instruction-Tuned
  Counterparts'
title_zh: 《事实召回的指令税：基座模型性能优于同架构指令调优版本》
authors:
- Christophe Khalil
- Aya Mourad
affiliations:
- American University of Beirut
- Sorbonne Université
arxiv_id: '2610.28407'
url: https://arxiv.org/abs/2610.28407
pdf_url: https://arxiv.org/pdf/2610.28407
published: '2026-10-20'
collected: '2026-10-21'
category: LLM
direction: 大模型事实召回 · 指令调优副作用分析
tags:
- FactualRecall
- InstructionTuning
- BaseModel
- KnowledgeGraph
- ClosedBookInference
one_liner: 发现指令调优存在事实召回损失的指令税，用基座模型+多采样策略在闭卷知识补全任务上得分超基线两倍
practical_value: '- 电商/广告领域做闭卷事实查询（商品属性、品牌信息、用户标签等）时，可优先测试Base Model的文本补全能力，无需默认选择Instruction
  Tuned版本，可直接提升事实准确率

  - 低资源模型选型时，可复用1GPU小时的快速知识探针方法，用100条以内标注样本测试不同模型版本的事实召回上限，大幅降低选型成本

  - 针对需要拒答的业务场景（无匹配商品、无效Query等），可采用单Query多采样+重复率阈值的策略，结合前置存在性校验，大幅提升拒答准确率，减少幻觉

  - 长尾知识召回场景可采用「多采样粗筛 + 小样本二阶段验证」的策略，无需引入RAG即可提升召回率'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
闭卷场景下从LLM预训练参数中抽取事实知识是知识图谱补全、语义搜索、无外挂Agent推理的核心能力，但现有方案普遍默认采用Instruction Tuned模型，忽略了指令调优可能带来的事实召回损失，且缺乏低成本的模型选型和事实抽取方案。

### 方法关键点
- 提出1GPU小时的快速知识探针方法，通过100条标注样本测试Base/Instruction Tuned模型的投票准确率和召回上限，快速完成选型
- 采用Base Model的文本补全范式替代问答/指令范式，搭配适配业务的few-shot补全模板引导输出，无需对齐指令
- 单Query采样64~256次，仅保留重复率超过关系专属阈值的结果，无符合要求结果时自动拒答
- 针对大答案集任务增加二阶段验证步骤，针对存在性判断类任务增加前置校验，过滤无效Query

### 关键实验
在AKBC 2026 LM-KBC闭卷知识补全任务上（475条测试样本，6类关系，20%样本需拒答），Base版Gemma-3-27B方案得分0.684，是官方基线0.296的2.3倍，比同架构Instruction Tuned版的0.568高11.6个百分点；其中数值类关系提升最明显，面积召回提升20.3个百分点，容量召回提升15.6个百分点；拒答决策F1达0.798。

### 最值得记住的一句话
事实召回场景下，Instruction Tuning并非总是最优选择，知道什么时候不回答，和知道答案本身几乎一样重要。
