---
title: From Reasoning Failures to Composable Video Spatial Intelligence
title_zh: 从推理失败到可组合的视频空间智能
authors:
- Pengzhan Sun
- Junbin Xiao
- Ramanathan Rajaraman
- Shiu-hong Kao
- Angela Yao
affiliations:
- National University of Singapore
- University of Science and Technology of China
arxiv_id: '2610.01999'
url: https://arxiv.org/abs/2610.01999
pdf_url: https://arxiv.org/pdf/2610.01999
published: '2026-10-01'
collected: '2026-10-03'
category: Multimodal
direction: 多模态大模型 · 空间推理优化
tags:
- VLM
- Spatial Reasoning
- Composable Operator
- Video Understanding
- Zero Training
one_liner: 拆解VLM空间推理错误根因，提出无训练几何算子库CROSS提升视频空间推理性能
practical_value: '- 大模型推理优化不要盲目做SFT/LoRA微调，可先做错误根因拆解，用训练无关的工具算子库补全能力缺口，大幅降低业务优化成本

  - 多模态Agent（如电商短视频理解、AR导购空间识别Agent）可参考分层能力拆解思路，将感知、几何计算、逻辑推理拆为独立模块，用可组合算子替代端到端推理，提升结果稳定性

  - 业务效果评估不要仅看整体任务准确率，可基于任务拆解的能力维度做错误归因，快速定位迭代方向，比如多模态内容召回错误可拆分感知、匹配、排序各环节根因'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
当前多模态空间推理基准仅输出任务级准确率，无法定位推理失败的根因，端到端优化难以针对性修复系统性错误，效率低下。
### 方法关键点
1. 基于共享坐标约定与统一schema对比预测值和真值的空间上下文，拆解出4类高频错误：感知不准、空间上下文缺失、度量选择错误、参考系/位姿跟踪错误；
2. 提出training-free的CROSS库，包含类型化几何算子与空间技能集，既可为非编码VLM输入校验后的上下文，也可作为可调用技能对接SpatialClaw Agent。
### 关键结果
在5个基准测试集上验证：ReVSI基准平均得分从55.9%提升至60.2%，DSI-Bench基准上SpatialClaw Agent得分从62.8%提升至66.3%，无需额外训练即可通过显式空间规则处理修复推理错误。
