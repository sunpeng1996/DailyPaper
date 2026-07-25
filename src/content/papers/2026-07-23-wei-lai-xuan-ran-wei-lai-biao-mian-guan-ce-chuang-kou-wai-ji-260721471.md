---
title: 'Future Rendering $\neq$ Future Surface: A Benchmark and Dataset for Dynamic
  Surface Reconstruction Beyond the Observed Window'
title_zh: 未来渲染≠未来表面：观测窗口外动态表面重建基准与数据集
authors:
- Yukun Shi
- Minglun Gong
affiliations:
- University of Guelph
arxiv_id: '2607.21471'
url: https://arxiv.org/abs/2607.21471
pdf_url: https://arxiv.org/pdf/2607.21471
published: '2026-07-23'
collected: '2026-07-25'
category: Other
direction: 动态3D表面重建 · 基准数据集构建
tags:
- 3D Reconstruction
- Benchmark Dataset
- Dynamic Scene
- Future Prediction
- Evaluation Metric
one_liner: 推出FutureSurf基准数据集，验证未来渲染质量与表面精度解耦，填补超观测窗口动态表面重建评估空白
practical_value: '- 仅面向涉及电商AR导购、虚拟试穿/试戴、3D内容动态预测的业务线，可复用其「前75%观测训练+后25%未来评估」的序列拆分范式

  - 3D内容生成效果验证环节，可参考其区分渲染质量与几何精度的评估逻辑，避免仅用PSNR等渲染指标误判几何还原效果

  - 普通电商推荐、搜索、Agent业务无直接适配场景，可借鉴价值有限'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有动态场景重建评估仅局限于观测时间窗口内，无法适配AR交互、机器人预判等场景对超观测窗口未来表面几何重建的评估需求，领域无统一评估基准。
### 方法关键点
推出FutureSurf可控诊断基准与数据集，以精确未来真值为核心牺牲部分场景多样性，包含8种分析定义的可控运动（含3种证伪控制）与逐帧真值网格；核心评估指标为未来帧表面Chamfer距离（CD），同时输出未来/观测CD差距作为诊断指标，配套发布拆分文件、评分代码、元数据。
### 关键结果数字
现有DG-Mesh骨干在原理上可预测的未来场景下仍存在2.7~4.1×的CD差距，Deformable-3DGS骨干差距达2.0~6.6×；未来渲染质量与表面精度统计上完全解耦，现有新视角合成指标无法表征未来几何精度，表面误差集中于运动区域。
