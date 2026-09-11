---
title: 'StudyBench: Can Self-Evolution Squeeze Textbooks for Olympiad Capability?'
title_zh: StudyBench：自进化方法能否从教材提炼奥赛解题能力
authors:
- Yinghao Chen
- Zixi Chen
- Bingxiang He
- Ziqing Qiao
- Huan-ang Gao
- Yinuo Xu
- Yuxin Zuo
- Zeyuan Liu
- Yuhao Zhan
- Chaojun Xiao
affiliations:
- Tsinghua University
- Zhejiang University
arxiv_id: '2609.00787'
url: https://arxiv.org/abs/2609.00787
pdf_url: https://arxiv.org/pdf/2609.00787
published: '2026-08-31'
collected: '2026-09-11'
category: Eval
direction: 大模型自进化能力评测
tags:
- Self-Evolution
- LLM Evaluation
- Reasoning
- Benchmark
- Knowledge Transfer
one_liner: 推出物理领域自进化能力评测基准StudyBench，量化知识吸收与迁移转化效率
practical_value: '- 做Agent自进化迭代时，可借鉴其拆分「知识吸收+迁移能力」的两层评测体系，避免仅在训练域内虚高的性能提升，更准评估落地泛化性

  - 做领域RAG/微调效果验证时，可参考其区分「应用级匹配」和「跨场景迁移」的测试集构造方法，避免评测结果和线上实际效果脱节

  - 做模型迭代资源分配时，可参考其Compute Plateau结论，避免盲目堆算力投入，优先优化自进化方法本身来突破性能瓶颈'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有大模型自进化方法缺乏标准化评测体系，无法量化从原始训练材料到可迁移解题能力的转化效率，难以判断性能提升的本质来源。
### 方法关键点
推出可控物理领域评测基准StudyBench，测试集拆分两类：① Application Set：收录高难度教材习题，评测知识吸收能力；② Transfer Set：收录奥赛级难题，评测跨场景知识迁移能力，覆盖3类不同基座模型测试主流自进化方法。
### 关键结果
1. Application Set上的性能提升极少能迁移到难度更高的Transfer Set；
2. 存在Guidance Gap：即使最强自进化方法，仅能达到同材料作为in-context guidance时效果的极小部分；
3. 所有自进化方法均存在Compute Plateau，远未耗尽算力预算时性能就已饱和，剩余差距核心来自方法缺陷而非数据或算力不足。
