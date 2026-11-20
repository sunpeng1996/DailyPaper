---
title: 'LSP-RAG: Latent Scoring Perspectives for Knowledge Graph Retrieval-Augmented
  Generation'
title_zh: LSP-RAG：基于隐式多视角打分的知识图谱检索增强生成框架
authors:
- Haochen Liu
- Guanghui Min
- Song Wang
- Yada Zhu
- Chen Chen
- Jundong Li
affiliations:
- University of Virginia
- University of Central Florida
- IBM Research
arxiv_id: '2611.25229'
url: https://arxiv.org/abs/2611.25229
pdf_url: https://arxiv.org/pdf/2611.25229
published: '2026-11-18'
collected: '2026-11-20'
category: RAG
direction: 检索增强生成 · KG-RAG多跳推理优化
tags:
- KG-RAG
- Soft Prompt
- Multi-hop Reasoning
- Lightweight LLM
- Retrieval Scoring
one_liner: 用轻量LLM结合双软提示多视角打分实现低成本高性能KG-RAG多跳推理
practical_value: '- 电商商品知识图谱、用户行为关联KG场景可直接复用双软提示打分逻辑，无需大模型即可实现低成本多跳召回，适配「适合过敏体质宝宝的高铁便携辅食」这类多属性关联的复杂用户查询，大幅提升召回准确率

  - 多视角打分+自适应聚合的trick可迁移到推荐系统的多路召回排序层，替代单一语义相似度排序，适配异构用户意图信号（同时存在价格敏感、品牌偏好、功能需求等多维度诉求的场景）

  - 动态更新上下文软提示的思路可用于Agent多轮工具调用的链路排序，避免多步调用过程中偏离初始用户需求，提升多轮复杂任务的完成率

  - 轻量LLM冻结仅调软提示+浅层头的训练方式上线成本极低，适合业务上快速迭代冷启动的KG相关RAG场景，无需大量标注数据即可快速上线'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有KG-RAG方案存在两类核心痛点：一是依赖ChatGPT等大模型引导检索，算力成本极高，无法适配大规模实时业务场景；二是采用轻量模型的方案多使用单一打分逻辑，无法适配异构相关性信号，也无法建模多跳推理的上下文依赖，易出现有效路径断裂、召回噪声过高的问题，多跳场景下性能表现极差。
### 方法关键点
- 设计双软提示驱动的多视角隐式打分模块：每个打分视角对应独立可学习的视角专属Soft Prompt，无需人工定义语义标签，自动适配直接匹配、间接关联、时间关联等异构相关性信号
- 新增动态更新的上下文Soft Prompt：每轮检索完成后，聚合前一轮所有候选三元组的打分隐向量更新上下文提示，将多步推理历史融入当前候选打分，避免孤立判断三元组相关性导致的有效路径丢失
- 多视角打分结果通过自适应门控网络加权聚合得到最终得分，每轮保留Top-M高分三元组扩展下一跳检索节点，全程仅微调软提示和浅层映射层，轻量LLM backbone完全冻结，训练和推理成本极低
### 关键实验
在WebQSP、WikiMovies、MetaQA 1-hop/2-hop四个KGQA基准数据集上测试，对比ToG、RoG等SOTA基线：基于Flan-T5-3B的LSP-RAG在WebQSP上准确率达88.59%，较使用ChatGPT做检索的ToG基线高出14.35个百分点；在所有数据集上，轻量LLM版LSP-RAG性能均超过采用大模型检索的基线，推理成本仅为后者的1/10以下。消融实验显示移除两类软提示后，准确率最高下降17个百分点，验证了核心组件的有效性。
### 核心结论
轻量模型搭配合理的归纳偏置设计，完全可以在知识密集型多跳推理任务上超过成本数倍的大模型方案
