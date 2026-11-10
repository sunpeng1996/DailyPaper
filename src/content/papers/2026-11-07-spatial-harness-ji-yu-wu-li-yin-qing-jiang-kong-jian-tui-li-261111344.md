---
title: 'Spatial Harness: Grounding Spatial Reasoning in Executable World States with
  Physics Engines'
title_zh: Spatial Harness：基于物理引擎将空间推理锚定到可执行世界状态
authors:
- Chentao Cao
- Zhanke Zhou
- Sangni Duan
- Bo Han
- Hang Li
affiliations:
- Hong Kong Baptist University
- ByteDance Seed
arxiv_id: '2611.11344'
url: https://arxiv.org/abs/2611.11344
pdf_url: https://arxiv.org/pdf/2611.11344
published: '2026-11-07'
collected: '2026-11-10'
category: Reasoning
direction: 多模态大模型 · 空间推理优化
tags:
- Spatial Reasoning
- Vision-Language Model
- Physics Engine
- World State
- Grounding
one_liner: 提出锚定物理引擎反馈的显式可执行世界状态框架，大幅提升VLM空间推理准确率
practical_value: '- 电商AR/3D导购Agent可复用该框架：将商品、用户视角显式建模为可执行世界状态，用物理引擎校验空间变换合理性，避免VLM生成不符合空间逻辑的导购建议（如推荐的家具无法放入用户户型）

  - 涉及空间交互的多模态Agent（如线下导购机器人、仓储盘点Agent）可借鉴其约束融合思路：将用户指令提取的空间约束与视觉感知结果对齐到统一坐标系，降低感知推理误差

  - 空间推理类任务评测可借鉴该方案：用物理引擎生成的可验证标注替代人工标注，降低评测成本，同时规避模型内部推理的作弊风险'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有VLM的空间推理依赖内部隐式场景表示，易出现场景理解错误，且想象的空间变换不满足物理约束，准确率受限。
### 方法关键点
- Spatial Harness将场景建模为显式可执行世界状态，引入物理引擎反馈锚定推理过程
- Perceiver模块融合问题提取的场景约束与视觉估计结果，将物体、相机对齐到统一坐标帧
- 物理引擎实例化世界状态后，Reasoner模块执行视角变换等操作，用计算得到的测量值、渲染视图引导推理，避免隐式想象误差
### 关键结果
在MindCube数据集上，将Qwen3.5-27B的准确率从52.70%提升至71.14%，比pySpatial高7.52个百分点；使用相同标注的物体和相机位姿时，框架准确率达98.25%，远高于模型内部推理的71.81%。
