---
title: 'OmniEcho: Spatial Audio Understanding for Embodied Agents'
title_zh: OmniEcho：面向具身Agent的空间音频理解框架
authors:
- Ruixun Liu
- Yuxuan Wang
- Jiacheng Xie
- Yuhuan You
- Donghua Cai
- Junming Lin
- Xiong-Hui Chen
- Zhifang Guo
- Yunfei Chu
- Qize Yang
affiliations:
- 北京大学
- 北京大学通用人工智能国家重点实验室
- 阿里巴巴集团Alibaba Token Hub
- 清华大学
arxiv_id: '2609.23407'
url: https://arxiv.org/abs/2609.23407
pdf_url: https://arxiv.org/pdf/2609.23407
published: '2026-09-19'
collected: '2026-09-25'
category: Agent
direction: 具身Agent · 多模态空间感知导航
tags:
- Embodied_Agent
- Spatial_Audio
- Multimodal_Perception
- Navigation_Benchmark
- Omni_Modal
one_liner: 提出含6类任务的空间音视觉导航基准，及带FOA空间编码器的多模态具身理解模型
practical_value: '- 做AR/VR电商导购具身Agent时，可引入FOA空间音频编码器补全多模态感知信号，提升室内场景定位与路径规划准确率

  - 多模态训练数据生成可复用本文的可控渲染管线，保证不同模态信号间的几何一致性，降低实采标注成本

  - 涉及线下导购/仓储巡检等具身Agent落地场景时，可参考OmniEchoBench的任务设计搭建自定义评测集，对齐真实业务需求'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有具身Agent感知推理依赖视觉+语言信号，缺少空间音频的有效建模与统一评测框架，无法复现人类融合多模态信号的场景理解能力。
### 方法关键点
1. 构建OmniEchoBench基准，覆盖6类空间音视觉感知、音视语言导航任务，包含197个真实场景、2972个QA对、900条带FOA音频的导航样本；
2. 研发空间音频可控渲染管线，保证声源、视觉观测、Agent轨迹的几何一致性，实现可扩展训练监督；
3. 提出OmniEcho多模态模型，新增FOA空间编码器搭配预训练语义音频通路，实现空间感知能力。
### 关键结果数字
空间音视觉感知任务达到SOTA，声音引导导航性能接近传统视觉语言导航水平，验证空间音频可作为具身推理的有效补充信号。
