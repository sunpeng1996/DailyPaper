---
title: 'SPARGen: Unifying Spatial Perception and Reasoning through Native Multimodal
  Generation'
title_zh: SPARGen：基于原生多模态生成的统一空间感知与推理框架
authors:
- Jinsheng Quan
- Jianhua Li
- Siyi Xie
- Xuanke Shi
- Kewang Deng
- Zukai Chen
- Feifei Shao
- Lei Yang
- Quan Wang
- Yawei Luo
affiliations:
- Zhejiang University
- SenseTime Research
- Peking University
arxiv_id: '2608.14138'
url: https://arxiv.org/abs/2608.14138
pdf_url: https://arxiv.org/pdf/2608.14138
published: '2026-08-13'
collected: '2026-08-17'
category: Multimodal
direction: 多模态大模型 · 空间感知推理统一
tags:
- Multimodal LLM
- Spatial Perception
- 3D Reconstruction
- Instruction Tuning
- Generative Model
one_liner: 用统一原生多模态生成框架同时支撑3D重建、稠密匹配、空间推理三类异构空间任务
practical_value: '- 电商3D商品建模、AR导购场景可复用统一多模态生成思路，无需为3D重建、空间语义推理单独开发任务专属模型，降低研发维护成本

  - 具身Agent空间导航、交互场景可参考将异构空间任务统一为instruction-conditioned生成范式，提升不同空间任务间的知识迁移效率

  - 多模态生成系统设计可借鉴「序列化token输出+图像对齐稠密几何场生成」的并行架构，同时满足结构化语义输出与像素级几何输出需求'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有空间感知与推理任务多采用任务专属架构或外部几何模块单独实现，同一场景不同互补表示间的知识传递受限，多任务部署成本高。
### 方法关键点
1 将3D reconstruction、dense correspondence、空间推理三类异构任务全部转化为instruction-conditioned生成任务，用单一原生多模态生成模型支撑
2 支持双路输出：将紧凑结构化、语言类输出序列化为token序列，同步生成与输入图像对齐的稠密几何场
3 引入空间监督信号联合优化模型共享表示，无需额外任务特定模块
### 关键结果
在3D重建、稠密匹配、空间推理三类公开基准上，单模型即可取得与各任务专属方案可比的竞争力性能
