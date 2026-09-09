---
title: 'Tool Retrievers Are Underestimated: Annotation Expansion Reveals True Capability'
title_zh: 工具检索器能力被低估：标注扩展还原真实性能
authors:
- Yanyu Zhu
- Chenheng Zhang
- Shaoshen Chen
- Hoilam Pao
- Yufei zhang
- Jiajun Chai
- Dongnian Wang
- Zhaoyu Hu
- Guojun Yin
- Wei Lin
affiliations:
- Tsinghua University
- Peking University
- Meituan
arxiv_id: '2609.08327'
url: https://arxiv.org/abs/2609.08327
pdf_url: https://arxiv.org/pdf/2609.08327
published: '2026-09-08'
collected: '2026-09-09'
category: Agent
direction: Agent工具检索 · 基准评测优化
tags:
- Tool Retrieval
- LLM Agent
- Benchmark
- Evaluation
- Annotation Expansion
one_liner: 提出自动标注扩展框架ToolEX，修正工具检索基准的一对一标注偏差，还原检索器真实性能
practical_value: '- 做Agent工具/技能检索评测时，可复用ToolEX的三阶段标注扩展流程，修正一对一标注偏差，尤其适合电商场景下大量功能重叠的服务商API/工具的检索评测，避免低估召回效果

  - 工具检索优化不要盲目迷信fine-tuning的指标提升，最多47%的增益可能是标注偏差导致的，建议同时上报精确匹配、功能等价匹配双指标，减少benchmark过拟合

  - 复合查询的工具检索可复用「拆分子查询+RRF融合结果」的架构，实验显示该方案能让零样本Qwen3-Embedding-0.6B的NDCG@10提升12.6pp，无需修改检索模型参数即可获得显著收益

  - 电商商品/服务检索场景若存在大量功能等价的不同供给，可参考ToolEX的等价标注思路优化召回评测指标，避免将有效召回结果误判为负例'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
开放域LLM Agent的工具库普遍存在大量功能重叠的工具，query与工具的映射天然是一对多关系，但现有工具检索基准仅标注单组ground truth，导致检索到有效等价工具时被误判为错误，系统性低估检索器性能，且虚增fine-tuning的效果增益。

### 方法关键点
- 三阶段自动标注框架ToolEX：① 用DeepSeek-V3.2将复合query拆分为与原标注工具一一对应的原子子查询，不暴露工具名称；② 每个子查询用Qwen3-Embedding-4B召回top20候选，GPT-4o-mini验证功能等价性；③ 候选工具做笛卡尔积后经RRF排序，Claude-Sonnet-5审核功能覆盖与依赖一致性，输出有效等价组合。
- 新评测基准ToolEq：每个query对应多组有效等价工具组合，评测时取所有等价组合的最高IR指标作为最终得分。

### 关键结果
在7360条query的Tool-DE基准上扩展后，平均每个query得到5.3组有效等价组合，67.9%的子查询存在至少1个等价工具；8个基础检索器的NDCG@10平均提升5~7pp；原有fine-tuning增益的30%~47%为标注偏差带来的虚假收益；拆分子查询+RRF融合的方案可让零样本检索器NDCG@10提升12.6pp；下游ToolBench任务通过率比原有基准最高提升6.9pp。

### 核心结论
开放工具生态下的检索评测应同时报告精确匹配和功能等价匹配得分，避免被单标注基准的虚假增益误导。
