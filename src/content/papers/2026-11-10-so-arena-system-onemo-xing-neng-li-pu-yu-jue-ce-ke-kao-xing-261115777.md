---
title: 'SO-Arena: Benchmarking the Capability Spectrum and Reliability of System One
  Models'
title_zh: SO-Arena：System One模型能力谱与决策可靠性评测基准
authors:
- Lichen Li
- Ziping Dong
- Sicheng Feng
- Qi Li
- Xinchao Wang
affiliations:
- National University of Singapore
arxiv_id: '2611.15777'
url: https://arxiv.org/abs/2611.15777
pdf_url: https://arxiv.org/pdf/2611.15777
published: '2026-11-10'
collected: '2026-11-14'
category: Eval
direction: 大模型评估 · System One模型能力评测
tags:
- Benchmark
- System One Model
- Evaluation
- Reliability
- Capability Assessment
one_liner: 提出覆盖11域5类能力的SO-Arena基准，可评测System One模型的能力谱与决策可靠性
practical_value: '- 评估业务侧快速决策类Agent（如推荐候选截断、广告实时出价）时，可复用SO-Arena的双维度可靠性评估框架：选项集变动稳定性、无有效选项识别能力，避免仅看准确率误判模型可用性

  - 做LLM4Rec/生成式推荐效果验证时，可借鉴证据锚定的标签校验、分域难度分层的评估设计，提升benchmark与业务效果的相关性

  - 落地System One类轻量化推理模型时，可参考结论：性能高≠决策可靠，上线前需额外增加稳定性校验环节，规避极端case故障'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有System One模型（无需长token生成的快速决策模型）评估仅关注聚合准确率，对能力覆盖广度、决策可靠性的刻画不足，无法系统分析模型优劣势。
### 方法关键点
1. 构建SO-Arena基准，覆盖11个领域、5类能力族，支持证据锚定的标签校验、分域难度分层评估、沙箱交互式仿真，同时可支撑System One/Two模型的推理能力对比
2. 新增双维度可靠性评估指标：选项集受控变动下的决策稳定性、无有效选项时的缺答案识别能力
### 关键结果
对21款模型测评发现：模型缩放与推理增强的收益在不同领域差异极大；性能最优的System One模型可靠性仅排第7，准确率与可靠性无强相关性
