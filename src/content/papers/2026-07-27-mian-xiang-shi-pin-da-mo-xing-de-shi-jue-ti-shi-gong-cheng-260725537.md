---
title: Visual prompt engineering for video models
title_zh: 面向视频大模型的视觉提示工程（VIPE）
authors:
- Robert Geirhos
- Yuxuan Li
- Thaddäus Wiedemer
- Neha Kalibhat
- Zi Wang
- Mani Malek
- Oyvind Tafjord
- Kevin Swersky
- Been Kim
- Priyank Jaini
affiliations:
- Google DeepMind
arxiv_id: '2607.25537'
url: https://arxiv.org/abs/2607.25537
pdf_url: https://arxiv.org/pdf/2607.25537
published: '2026-07-27'
collected: '2026-07-30'
category: Multimodal
direction: 多模态视觉推理 · 视觉提示工程
tags:
- Visual Prompt Engineering
- Video Foundation Model
- Visual Reasoning
- Multimodal Optimization
- VIPE
one_liner: 提出针对视频大模型的视觉提示工程VIPE，无需改模型效果优于文本提示与测试时缩放
practical_value: '- 多模态电商推荐场景可复用VIPE思路，对输入的商品短视频/图像做预处理（如线稿转实拍、模糊转高清、抽象场景转写实），无需调整推荐模型即可提升多模态特征提取精度

  - 电商Agent处理视觉类任务（如用户上传场景图的商品匹配、短视频中的商品识别）时，可引入轻量图像编辑模型做输入优化，替代成本更高的LoRA微调

  - 资源有限的业务场景优先尝试输入侧prompt（含文本、视觉）优化，优先级高于测试时缩放或小样本微调，投入产出比更高'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
文本prompt工程已成为LLM性能优化的标准手段，但当前视频视觉大模型的性能优化仍依赖文本prompt、测试时缩放等方案，未探索视觉输入本身的优化空间，无法充分释放视频大模型的推理能力。

### 方法关键点
视觉提示工程（VIPE）范式：无需修改视频模型的权重与架构，仅通过调用图像编辑模型，对输入给视频模型的初始视觉素材做自动转换（如将抽象线稿场景转为照片级写实场景），优化视觉输入的信息表达。

### 关键结果
在多类视频推理任务上实现稳定性能提升，效果优于传统文本prompt工程、测试时缩放两种常用优化策略，计算成本远低于模型微调，是低投入的视频大模型性能优化方案。
