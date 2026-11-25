---
title: 'Nemotron-Labs-VisualCreation: Pixel as Code for Agentic Visual Creation'
title_zh: Nemotron-Labs视觉生成框架：面向智能体视觉创作的像素即代码方案
authors:
- Guo Chen
- Fuxiao Liu
- Haoqin Tu
- Yiyang Zhou
- Andrew Tao
- Bryan Catanzaro
- Cihang Xie
- Yuyin Zhou
- Huaxiu Yao
- Didong Lu
affiliations:
- NVIDIA
arxiv_id: '2611.31358'
url: https://arxiv.org/abs/2611.31358
pdf_url: https://arxiv.org/pdf/2611.31358
published: '2026-11-22'
collected: '2026-11-25'
category: Agent
direction: Agent 智能体视觉生成 · 多模态协同
tags:
- Agentic Generation
- Visual Tokenizer
- Multimodal LLM
- Pixel as Code
- Reinforcement Learning
one_liner: 提出Pixel as Code统一接口，打造多组件协同的智能体视觉生成框架，性能比肩GPT Image 2
practical_value: '- 电商商品图、营销海报、详情页生成场景可复用「视觉token生成+结构化代码渲染」的混合架构，既保证视觉效果又支持后续布局、文本的二次编辑，降低运营修图成本

  - 生成结果校验环节可借鉴其「渲染器确定性检查+多模态VLM打分」的双层质检逻辑，同时结合根因定位做定向修复，大幅提升生成内容的合规性和符合度

  - 大模型生成优化可复用其基于GRPO的组相对策略优化方法，通过同prompt多候选的奖励差异做强化学习，显著提升生成内容的prompt对齐度'
score: 9
source: huggingface-daily
depth: full_pdf
---

### 动机
现有视觉生成方案要么仅输出不可编辑的静态栅格图像，无法满足电商、办公场景下布局调整、文本修改的需求；要么结构化生成精度不足，难以同时兼顾视觉表现力和可控性，亟需统一框架打通栅格生成、结构化代码生成与智能体规划校验链路。
### 方法关键点
- 提出**Pixel as Code**统一接口：栅格图像用离散视觉token表示，结构化产物（SVG/HTML/LaTeX等）用显式代码表示，两者通过统一的「生成表示→渲染输出→结果校验」流程协同，支持混合产物生成
- 自研全链路核心组件：包括642M参数的Nemotron-Labs-Image-Tokenizer，30B参数的自回归栅格生成器Nemotron-Labs-Image-30B-A3B，以及结构化代码生成模型家族Nemotron-Labs-VisionCode
- 智能体动态编排逻辑：根据用户请求自动路由生成路径，栅格生成采用多候选VLM选优，结构化生成采用双编码器生成+根因定位定向修复的迭代流程，最多支持3轮修复
- 训练优化策略：图像tokenizer结合重建损失、感知损失、特征蒸馏和对抗训练；生成器采用多阶段渐进分辨率训练+GRPO强化学习优化prompt对齐度
### 关键实验结果
- 图像tokenizer在178K跨6个领域的图像集上，PSNR较Emu3.5 IBQ从26.08提升到29.57dB，单batch A100上编码快7.13倍、解码快10.93倍
- VisionCode模型在Chart2Code、MMSVG等5个任务的综合得分超过Kimi K3.1 Pro
- 系统级评估中，相同栅格生成器下GenEval2 Soft-TIFA GM从31.71提升到52.56，最优配置性能在多数基准上比肩GPT Image 2和Nano Banana Pro
> 最值得记住的一句话：将视觉生成的离散表示和结构化代码通过统一渲染接口对齐，是实现兼顾表现力、可控性和可编辑性的智能体视觉生成的核心路径
