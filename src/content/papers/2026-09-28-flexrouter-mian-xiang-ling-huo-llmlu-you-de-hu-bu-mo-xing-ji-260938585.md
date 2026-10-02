---
title: 'FlexRouter: Learning Complementary Model Sets for Flexible LLM Routing'
title_zh: FlexRouter：面向灵活LLM路由的互补模型集学习方法
authors:
- Wang Wei
- Harry Yang
- Tiankai Yang
- Samyadeep Basu
- Hongjie Chen
- Andy Zhao
- Franck Dernoncourt
- Ryan A. Rossi
- Hoda Eldardiry
affiliations:
- Virginia Tech
- University of Southern California
- Adobe Research
- Dolby Labs
arxiv_id: '2609.38585'
url: https://arxiv.org/abs/2609.38585
pdf_url: https://arxiv.org/pdf/2609.38585
published: '2026-09-28'
collected: '2026-10-02'
category: LLM
direction: LLM路由 · 互补模型子集选择
tags:
- LLM Routing
- Determinantal Point Processes
- Coverage Optimization
- Adaptive Inference
- Model Complementarity
one_liner: 基于DPP建模LLM互补性，实现无固定预算的高覆盖低冗余LLM路由
practical_value: '- 多LLM调用的Agent系统（如电商智能客服、多模型兜底文案生成）可直接复用DPP建模模型互补性的思路，替代传统top-k选模型策略，降低冗余调用成本，提升至少产出1个正确答案的概率

  - 推荐系统召回/多样性排序场景，可借鉴该覆盖导向的子集选择框架，用DPP同时建模item质量和相似度，优化用户长尾需求覆盖，还可通过自适应停止规则灵活控制召回规模

  - 工程上可复用基于边际增益的贪心选择+自适应停止策略，无需固定k值，仅调整阈值τ即可平衡效果和算力成本：参考τ=0.2时可减少35.9%的模型调用量，成功率仅下降1.13%'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM路由方法多独立对模型打分选top-k，忽略模型相关性，容易选到失效模式一致的冗余模型，导致整体正确率瓶颈；且固定算力预算无法适配不同难度query的资源需求，而工业界多模型管线核心目标是至少有1个模型输出正确结果供下游筛选，而非所有选中模型都得高分。

### 方法关键点
- 将路由建模为覆盖导向的子集选择问题，目标是最大化至少1个选中模型答对的概率，同时最小化冗余
- 用Determinantal Point Processes(DPP)参数化路由策略，核矩阵对角线为query依赖的模型能力得分，非对角线为模型间余弦相似度，天然兼顾模型质量和冗余惩罚
- 训练无需标注最优子集，通过对失效集边缘化设计覆盖损失，配合单模型正确性预测的BCE辅助损失稳定训练
- 推理采用基于边际行列式增益的贪心选择，加自适应停止规则，动态决定选中模型数，无需固定k值

### 关键实验
在RouterEval基准测试：中等模型池（3811个模型）下平均Success@10达0.8632，较基线高3个百分点，模型列表多样性ILD@10达0.762，是基线的3倍以上；大模型池（5000个模型）下平均Success@10达0.9914，较基线高1个百分点，跨领域泛化效果优于所有基线。

### 最值得记住的一句话
多模型选择的核心目标不是选得分最高的k个，而是选互补的模型集，最大化至少1个正确结果的覆盖概率，远好过冗余的高分重复。
