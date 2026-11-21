---
title: 'WM^MLLM: Turning MLLMs into World Models'
title_zh: WM^MLLM：将多模态大语言模型改造为世界模型
authors:
- Baiang Li
- Enze Xie
- Jincheng Yu
- Jin Wang
- Haozhe Liu
- Yitong Li
- Juanxi Tian
- Felix Heide
affiliations:
- Princeton University
- NVIDIA
- OpenEnvision
arxiv_id: '2611.24193'
url: https://arxiv.org/abs/2611.24193
pdf_url: https://arxiv.org/pdf/2611.24193
published: '2026-11-17'
collected: '2026-11-21'
category: Multimodal
direction: 多模态大模型 · 交互式世界模型构建
tags:
- MLLM
- World Model
- Interactive Generation
- Image Editing
- Panorama Generation
one_liner: 首个基于MLLM的交互式世界模型，支持单图生成可编辑、状态持久化的全景环境
practical_value: '- 电商虚拟逛店、3D商品展示场景可借鉴「状态外置+全景存储+版本管理」方案，解决视角切换内容漂移、编辑失效问题

  - 商品图修图、营销物料局部编辑场景可复用「先生成候选再选写入区域+校验」pipeline，编辑准确率可从34.8%提升至83.0%

  - 多模态Agent做环境交互类任务时，可引入持久化世界状态机制，避免交互过程中上下文丢失、前后逻辑矛盾'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
传统视频类世界模型将世界状态存储在生成器上下文内，存在视角复现漂移、局部编辑后非目标区域内容变更、修改历史无法追溯的问题，无法支持持久化交互式场景生成。

### 方法关键点
1. 将世界状态外置存储为带修订历史的全景图，不与生成器上下文绑定；
2. MLLM负责将用户请求（视角移动、文本/框选编辑、属性修改等）转化为全景状态操作，自动选择局部编辑写入区域，对生成候选校验后再更新状态；
3. 图像生成器仅负责生成视图，视频仅做呈现，全程基于上一次请求结果迭代。

### 关键结果
在MBench-A上对比6个基线，4项环境恢复指标均为第一，Epipolar指标达91.5（基线最高74.0），相机往返成功率85.3%（基线最高50.9%）；CompBench对比15个基线，15项指标全部最优；所有视角复现任务100%成功，通过校验的局部编辑100%不修改非目标区域像素。
