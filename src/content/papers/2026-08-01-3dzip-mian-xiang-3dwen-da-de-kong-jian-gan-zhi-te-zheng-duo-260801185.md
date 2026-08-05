---
title: '3DZip: Spatial-Aware Feature Diversity-Guided Token Compression for 3D Question
  Answering'
title_zh: 3DZip：面向3D问答的空间感知特征多样性引导Token压缩方法
authors:
- Changwoo Baek
- Kyeongbo Kong
affiliations:
- Pusan National University
arxiv_id: '2608.01185'
url: https://arxiv.org/abs/2608.01185
pdf_url: https://arxiv.org/pdf/2608.01185
published: '2026-08-01'
collected: '2026-08-05'
category: Multimodal
direction: 多模态大模型 · 3D场景Token压缩
tags:
- 3D-VLM
- Token Compression
- Determinantal Point Process
- 3D Question Answering
- Multimodal Reasoning
one_liner: 提出三阶段3D Token压缩框架，仅用128个Token保留94.7%原性能，推理提速1.92倍
practical_value: '- 多模态Agent处理3D场景（如AR/VR电商商品浏览、线下导购机器人）时，可复用三阶段压缩思路降低推理时延

  - 特征选择环节引入Determinantal Point Process保障多样性的策略，可迁移到多模态召回的Token去重场景，避免语义冗余

  - 空间约束下的Token合并方法，可用于空间感知类推荐（如线下LBS、AR试穿场景的多特征融合）降低计算开销'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
3D VLM需将2D视觉特征投影到世界坐标生成空间感知Token，单场景生成数千个Token带来极高计算、内存开销；现有2D VLM的Token压缩方案忽略3D Token的空间结构，仅靠空间聚合也无法解决对象级Token不平衡问题。
### 方法关键点
提出三阶段3DZip压缩框架：1）粗体素化去除点级冗余；2）通过Determinantal Point Process按特征空间多样性选择锚Token；3）空间约束下合并剩余Token，保留几何一致性。
### 关键结果
在3个3D问答基准上性能优于现有压缩方案，仅保留128个Token时可维持原模型94.7%的性能，推理速度提升1.92倍。
