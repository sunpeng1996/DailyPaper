---
title: Can Language Models Play the Wikipedia Game?
title_zh: 语言模型能否完成维基百科跳转游戏？
authors:
- Alexander Hickey
- Joanna Knight
- James Bishop
affiliations:
- The Alan Turing Institute
arxiv_id: '2610.13948'
url: https://arxiv.org/abs/2610.13948
pdf_url: https://arxiv.org/pdf/2610.13948
published: '2026-10-09'
collected: '2026-10-12'
category: Eval
direction: 大模型评测 · 知识图谱语义导航
tags:
- LLM Evaluation
- Knowledge Graph Navigation
- Sentence Embedding
- Reasoning LLM
- Wikipedia Game
one_liner: 基于维基百科跳转游戏评测多类语言模型的知识图谱语义导航能力
practical_value: '- 做知识图谱导航类Agent（如电商导购Agent从商品页跳转至目标品类、学术检索Agent）时，优先用轻量sentence
  embedding做候选初筛，再用小参数reasoning LLM做排序，性价比远高于直接调用大模型

  - 跨领域/跨语言部署语义匹配类任务时，不要默认通用大模型效果最优，需针对垂直领域（如电商美妆、3C类）单独测试embedding和LLM的效果，避免跨域性能跳水

  - 处理长候选列表的LLM选择任务时，控制单次prompt内的候选数量（如200条以内），可显著降低幻觉、提升任务成功率，可直接复用在推荐系统候选集重排场景

  - 对成本敏感、零容忍幻觉的语义导航任务，优先选用sentence embedding方案，其无幻觉、推理速度快，性能可超过多数中等规模LLM'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前LLM与embedding模型广泛用于非结构化文档检索、语义匹配等任务，但现有评测很少验证模型在需要连续语义关联、路径规划的导航类任务上的真实能力，跨语言、跨领域的性能差异也缺乏统一对照基准。
### 方法关键点
- 构建10个公开知识图谱数据集：含5种语言的维基百科链接图谱、5个垂直领域的OpenAlex学术文献引用图谱，规则为仅允许通过当前节点的边跳转，禁止倒推、提前预览后续节点
- 覆盖三类主流方法：sentence embedding（每步选与目标cosine相似度最高的节点）、原生生成式LLM、Chain-of-Thought推理LLM，基线为TF-IDF统计方法、人类玩家实测表现
- 统一评测规则：最多允许100步跳转，禁止重复访问节点，LLM幻觉输出最多重试4次修正
### 关键实验
在10个图谱上各测1万组可连通的<起点, 终点>对，英语维基百科额外补充9名人类玩家的109组测试结果：最佳推理LLM（GPT-o3 mini(R)）成功率与人类相当（≈75%），但平均步长比人类高30%以上；E5-Small等通用embedding模型成功率超70%，优于Llama3.1 70B等中等规模非推理LLM；同参数下推理LLM比非推理LLM成功率高20%~30%；通用大模型Llama3.1 405B迁移到学术领域时成功率下降约33%。
### 核心结论
在成本敏感、对幻觉零容忍的语义导航类任务中，轻量embedding模型的性价比远高于多数大语言模型，仅在需要长期路径规划的场景下才需要调用推理LLM。
