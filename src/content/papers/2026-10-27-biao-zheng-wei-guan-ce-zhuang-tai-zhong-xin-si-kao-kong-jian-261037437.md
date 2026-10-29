---
title: 'Representing the Unseen: Rethinking Visual Imagination for Spatial Reasoning'
title_zh: 表征未观测状态：重新思考空间推理的视觉想象表征选择
authors:
- Zengqi Zhao
- Zun Wang
- Shoubin Yu
- Mohit Bansal
- Yue Zhang
affiliations:
- UNC Chapel Hill
arxiv_id: '2610.37437'
url: https://arxiv.org/abs/2610.37437
pdf_url: https://arxiv.org/pdf/2610.37437
published: '2026-10-27'
collected: '2026-10-29'
category: Reasoning
direction: 空间推理 · 多模态表征自适应选择
tags:
- Spatial Reasoning
- Visual Representation
- World Model
- Multimodal
- Benchmark
one_liner: 提出ImagiRep空间推理基准与GEARS自适应表征选择策略，验证多表征相比单RGB的性能增益
practical_value: '- 电商AR导购、虚拟场景选品等涉及空间推理的Agent场景，不要默认仅用RGB作为唯一视觉表征，可新增深度、鸟瞰几何、全景图等互补表征，降低单一表征的推理误差

  - 推理任务可复用GEARS轻量测试时自适应选择逻辑，根据任务类型动态匹配最优表征，无需重训大模型，落地成本极低

  - 涉及多模态生成的推荐/搜索场景，可参考本研究结论，优先为下游推理任务优化表征，而非仅追求生成效果的逼真度'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
当前视觉世界模型做空间推理时默认生成RGB视图作为未观测状态的想象表征，但RGB是为生成效果优化，并非下游推理任务的最优选择，不同空间推理需求适配的表征存在显著差异。
### 方法关键点
1. 构建ImagiRep模拟器基准，覆盖视角想象、跨视图融合2类场景，7种问题类型共922条标注样本，为同一未观测状态提供真值RGB及深度、全景图、鸟瞰几何等6种替代表征；
2. 提出GEARS轻量测试时策略，无需重训模型即可根据任务类型自适应选择最优表征组合。
### 关键结果
即使完全准确的想象RGB也无法保证空间推理准确率，单一估计RGB甚至会误导推理，GEARS相比现有单RGB空间想象方法性能显著提升，替代表征可提供稳定互补增益。
