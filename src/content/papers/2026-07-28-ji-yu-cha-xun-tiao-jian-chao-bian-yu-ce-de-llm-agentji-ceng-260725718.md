---
title: 'Tools Are Not Islands: Set-Level Tool Retrieval for LLM Agents via Query-Conditioned
  Hyperedge Prediction'
title_zh: 基于查询条件超边预测的LLM Agent集层级工具检索框架HYSET
authors:
- Xinyi Hong
- Pinjun Dong
- Xinyang Yu
- Binyan Jiang
affiliations:
- Shanghai Jiao Tong University
- The Hong Kong Polytechnic University
arxiv_id: '2607.25718'
url: https://arxiv.org/abs/2607.25718
pdf_url: https://arxiv.org/pdf/2607.25718
published: '2026-07-28'
collected: '2026-07-29'
category: Agent
direction: Agent工具检索 · 超图建模
tags:
- Tool Retrieval
- Hypergraph
- LLM Agent
- Set-level Scoring
- Zero-shot Transfer
one_liner: 将LLM Agent工具检索建模为超边预测任务，实现集层级工具联合效用打分，性能优于现有SOTA方案
practical_value: '- 做Agent工具检索/电商组合推荐场景时，可直接复用HYSET作为前置筛选模块，无需修改下游Agent/推荐排序逻辑，就能提升工具集/商品组合的完整性

  - 建模不同大小集合的item交互时，可借鉴基数专属交互矩阵Mm的设计，仅用少量参数就能实现高阶交互，无需引入复杂的多阶张量，兼顾效果和计算效率

  - 大规模组合检索场景可复用两阶段推理trick：先单路召回高相关短列表，再做集层级重排，既能解决组合爆炸问题，又能召回低个体分但高互补性的item

  - 工具库/商品类目快速迭代的场景，可复用其少样本迁移能力，仅需每个新类目5个标注样本就能恢复93%+的全监督性能，降低标注成本'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有LLM Agent工具检索要么对单工具独立打分，要么顺序生成工具集，均未对工具集的联合效用做整体评估，导致高个体分工具冗余、互补工具漏选问题突出：ToolBench上最优单工具检索Recall@3达68.6%，但完整工具集覆盖率COMP@3仅39.7%；同时工具共调用模式和集合大小强相关，如汇率与天气工具在2工具集共现率仅0.4%，在4工具集则达23%，现有方法无法建模该依赖关系。

### 方法关键点
- 将工具检索建模为工具共调用超图上的查询条件超边预测任务，以整个工具集为打分单元，语义匹配、图增强、生成式三类现有检索范式均为该框架的受限实例
- 打分函数拆分为两部分：Fset建模工具集内部交互，用基数专属对称交互矩阵Mm捕捉不同大小集合下的工具兼容性，仅用O(Md²z)参数即可实现最高M阶交互，避免高维张量爆炸；Falign建模查询与工具集的对齐度，以查询嵌入为query对工具嵌入做交叉注意力池化，实现查询感知的集级适配
- 训练结合标注监督的检索损失、执行反馈的奖励加权自训练损失；推理采用两阶段流程：先单工具打分召回Kpool大小的短列表，再枚举短列表内所有合法大小的集合做重排，平衡效果与效率

### 关键实验
在ToolBench（1.6w+API、20w+指令）上对比6个SOTA基线，HYSET（Qwen2.5 backbone）相对最优基线COMP@5提升11.6%，端到端任务通过率提升13.1%；零样本迁移到新工具/新类目时，每个类目仅需5个标注样本即可恢复93.2%的全监督性能，推理延迟仅12.4ms/query，远低于生成式检索的378.4ms。

### 核心观点
工具不是孤岛，多工具的联合效用并非单工具价值的简单加和，集层级建模是提升复杂任务下工具检索完整性的核心路径
