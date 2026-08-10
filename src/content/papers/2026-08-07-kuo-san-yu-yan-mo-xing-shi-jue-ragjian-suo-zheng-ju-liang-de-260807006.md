---
title: Does More Retrieved Evidence Help Visual Retrieval-Augmented Generation with
  Diffusion Language Models?
title_zh: 扩散语言模型视觉RAG检索证据量的影响及免训练过滤方法
authors:
- Jiankun Wang
- Yisen Gao
- Ziwei Zhang
- Xingcheng Fu
- Jiaxin Bai
- Chen Gao
affiliations:
- Beihang University
- The Hong Kong University of Science and Technology
- Guangxi Normal University
- Hong Kong Baptist University
- National University of Singapore
arxiv_id: '2608.07006'
url: https://arxiv.org/abs/2608.07006
pdf_url: https://arxiv.org/pdf/2608.07006
published: '2026-08-07'
collected: '2026-08-10'
category: RAG
direction: 多模态RAG · 扩散大模型证据过滤
tags:
- RAG
- Diffusion Language Model
- Visual QA
- Training-free
- Evidence Filtering
one_liner: 发现扩散语言模型视觉RAG并非检索证据越多越好，提出免训练熵基候选过滤框架ECF提升准确率
practical_value: '- 搭建RAG系统时不要盲目扩大固定top-k检索数量，尤其是用并行解码/非自回归LLM时，多证据的语义冲突对生成质量的负面影响远大于召回提升的收益，建议先做冲突检测再决定是否引入额外证据

  - 可复用ECF的免训练证据过滤思路：仅通过LLM首步解码的答案块熵变化+同尺寸空白对照，就能低成本判断新增检索片段的正向价值，不需要额外训练排序模型或标注数据

  - 多粒度检索候选构建的trick可直接迁移到电商商品、商品详情页、文档类的RAG场景：将原始素材拆分为全局+局部区域作为检索单元，既能降低单条证据的无关内容占比，也能提升检索召回的灵活性

  - 调优RAG召回参数时，可将候选池大小和最终输入模型的上下文大小解耦：候选池可以适当扩大以提升召回覆盖，靠过滤模块筛选有效证据，避免直接增加输入的top-k数量导致的效果下降'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有视觉RAG默认向生成器输入尽可能多的top-k检索证据以提升答案覆盖，该假设对并行解码的Diffusion Language Models (DLMs)并不成立：实验显示召回率随k上升的同时，生成准确率反而持续下降，核心原因是多证据语义冲突导致DLM并行去噪时丢失源一致性，拼接不同来源的内容生成无依据的错误答案，现有自适应证据选择方法未适配DLM多源联合输入的并行生成特性，亟需针对性的优化方案。

### 方法关键点
- 多粒度证据构建：将单页文档拆分为全页+布局识别得到的最多3个局部区域作为检索候选，降低单条证据的无关内容占比
- 空白对照增益计算：以top-1检索结果为基准，对每个新增候选，分别计算其与同尺寸空白占位符搭配top-1时，DLM首步答案块的加权熵差，增益为正代表候选能降低生成不确定性、减少冲突风险
- 排序优先选择规则：始终保留top-1证据，仅当top-2的增益为正时才允许扩展上下文，更低排名的候选需要同时超过当前最优增益、且联合熵低于单独top-1才能替换默认扩展

### 关键实验
在ChartQA、DocVQA、InfoVQA等5个视觉QA基准、3个多模态DLM上测试，ECF相比最优固定top-k输入平均提升准确率2.62个百分点；基于LLaDA2.0-Uni时相比最优免训练baseline平均提升2.37个百分点；候选池大小从k=3扩大到k=5时效果保持稳定，不会像固定top-k方案那样出现准确率下降。

最值得记住的结论：**DLM的RAG系统中，更大的检索候选池只有配合前置的证据过滤机制才能带来收益，而非无条件将所有检索到的证据输入生成器**
