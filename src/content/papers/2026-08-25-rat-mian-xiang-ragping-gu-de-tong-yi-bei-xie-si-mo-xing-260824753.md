---
title: 'The RAT: A Unified Bayesian Model for RAG Evaluation'
title_zh: RAT：面向RAG评估的统一贝叶斯模型
authors:
- Pius von Däniken
- Felix Matthias Saaro
- Mark Cieliebak
- Jan Deriu
affiliations:
- ZHAW School of Engineering
arxiv_id: '2608.24753'
url: https://arxiv.org/abs/2608.24753
pdf_url: https://arxiv.org/pdf/2608.24753
published: '2026-08-25'
collected: '2026-08-26'
category: Eval
direction: RAG系统评估 · 贝叶斯概率建模
tags:
- RAG
- Evaluation
- Bayesian Model
- LLM-as-judge
- Annotation Efficiency
one_liner: 提出贝叶斯RAG评估框架，拆分任务成功与生成器合规性，优化标注分配并融合多源评测结果
practical_value: '- 评估自有RAG系统时，不要只看端到端正确率，需拆分检索成功率、拒答策略合规性、回答正确率三个维度，避免选中端到端效果接近但幻觉率高的方案

  - 标注预算有限时，若核心优化目标是生成器策略合规性（降幻觉、提升拒答准确率），优先标注检索是否成功，效率是标注回答正确性的2~3倍

  - 用LLM-as-judge做RAG评测前必须先校准FPR，高误报率的自动评测即使新增数千条样本，效果也远不如少量高质量人工标注

  - 这套贝叶斯因子化框架可直接复用在搜索推荐pipeline评估中，拆分召回、排序、生成各环节的误差传播，无需单独测试每个模块'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有RAG评估要么单独测试各模块，要么仅看端到端效果，无法区分端到端正确率背后的生成器策略差异：比如两个端到端效果相同的RAG系统，可能一个从不拒答、幻觉率高，另一个合理拒答、更符合业务要求，同时也缺乏标注预算分配的优化指导。

### 方法关键点
- 定义4个核心二元变量：检索成功R、拒答A、任务成功T、生成器合规G，按RAG pipeline信息流做贝叶斯因子化：$P(R,A,T) = P(R)P(A|R)P(T|A,R)$，G为基于R/A/T的确定性函数（检索失败时拒答/检索成功时答对即合规）
- 建模标注分配问题，基于信息增益对比不同标注组合的评估效率
- 扩展支持LLM-as-judge作为带噪观测，引入校准的TPR/FPR融合人工与自动标注结果

### 关键结果数字
覆盖3个数据集（FEVER/HotpotQA/NQ）、3种检索器、3种生成器共27组配置测试：
1. 端到端正确率接近的生成器，策略合规性差异可达3倍：NQ数据集上Apertus和Qwen3.5任务成功率均为0.24左右，合规性分别为0.16和0.49
2. 评估策略合规性时，纯检索标注的效率是纯任务标注的2~3倍，可达到全标注60%左右的效果
3. 高FPR的LLM-as-judge即使新增5000条样本，也仅能让策略合规性的95%置信区间宽度从0.094降到0.08，几乎无实质提升

### 核心结论
RAG系统的端到端正确率≠生成器策略合规性，优化标注投入和评测准确性的核心是拆解pipeline各环节的依赖关系，而非单纯堆评测样本量
