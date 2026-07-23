---
title: 'OrientSAM: Mitigating Camera-Centric Shortcut in Multimodal Spatial Reasoning
  via Orientation-Aware Spatial Alignment'
title_zh: OrientSAM：通过方向感知对齐缓解多模态空间推理的相机中心捷径
authors:
- Wenxiao Fan
- Hang Yin
- Kan Li
affiliations:
- School of Computer Science, Beijing Institute of Technology
arxiv_id: '2607.17657'
url: https://arxiv.org/abs/2607.17657
pdf_url: https://arxiv.org/pdf/2607.17657
published: '2026-07-20'
collected: '2026-07-23'
category: Multimodal
direction: 多模态大模型 · 空间推理优化
tags:
- MLLM
- Spatial Reasoning
- Multimodal Alignment
- Curriculum Learning
- Fourier Encoding
one_liner: 提出方向感知多模态空间对齐框架OrientSAM，解决MLLM空间推理依赖相机视角的系统误差问题
practical_value: '- 做多模态商品理解、AR实景导购、虚拟试穿类Agent时，可引入Fourier角度编码+方向感知token显式建模物体朝向，避免视角依赖的空间判断错误

  - 训练视角敏感的多模态任务时，可复用课程学习策略，从简单相机视角任务逐步过渡到非相机视角任务，提升模型泛化性

  - 若需批量生成空间推理标注数据，可参考论文的空间数据构造pipeline，基于现有图像自动生成朝向相关监督信号，降低标注成本'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
多模态大模型（MLLM）在需视角转换的空间推理任务中存在明显缺陷：普遍依赖相机视角线索而非参考物体视角进行推理，在非相机参考的场景下会出现系统性误差，核心原因是缺失对物体朝向的显式建模。
### 方法关键点
1. 提出OrientSAM方向感知空间对齐框架，通过方向感知token与傅里叶角度编码，将显式朝向信息注入多模态表征；
2. 采用课程学习策略，从易到难逐步训练模型的视角感知推理能力；
3. 搭建自动化空间数据构造流水线，可基于大规模图像生成朝向感知的空间监督信号。
### 关键结果
在Spatial-MM、ViewSpatial、3DSRBench三个公开基准上，OrientSAM效果全面优于现有强基线，尤其在非相机视角、以人为中心、朝向敏感任务上提升幅度最大，验证了显式朝向建模可有效缓解相机中心捷径问题。
