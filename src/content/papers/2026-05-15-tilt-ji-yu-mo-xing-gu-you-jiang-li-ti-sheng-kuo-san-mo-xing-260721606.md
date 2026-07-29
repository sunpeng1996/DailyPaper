---
title: 'TILT: Improving Compositional Generation in Diffusion Models with a Model-Intrinsic
  Reward'
title_zh: TILT：基于模型固有奖励提升扩散模型的组合生成能力
authors:
- Debottam Dutta
- Jaehoon Hahm
- Jianchong Chen
- Romit Roy Choudhury
affiliations:
- University of Illinois Urbana-Champaign
- Zhejiang University
arxiv_id: '2607.21606'
url: https://arxiv.org/abs/2607.21606
pdf_url: https://arxiv.org/pdf/2607.21606
published: '2026-05-15'
collected: '2026-07-29'
category: Multimodal
direction: 多模态生成 · 扩散模型组合性优化
tags:
- Diffusion Model
- Text-to-Image
- Compositional Generation
- Test-Time Alignment
- Reward Design
one_liner: 提出无训练的TILT框架，用扩散模型固有奖励提升复杂组合提示的生成对齐效果
practical_value: '- 电商多模态商品图生成场景可复用无额外训练的测试时奖励对齐思路，无需重训大模型即可提升"红色长款连衣裙配白色帆布鞋"这类复杂组合Prompt的生成准确率

  - 可借鉴模型固有奖励设计逻辑，无需外接独立奖励模型就能优化生成效果，降低推理链路复杂度和部署成本

  - 带KL约束的闭式采样优化方法可直接迁移到AIGC商品素材生成服务，平衡生成内容的Prompt对齐度与视觉质量'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有文生图扩散模型处理多概念组合的复杂Prompt时，常出现概念遗漏、优先级偏移的组合生成错误，现有优化方案多需额外训练或外接奖励模型，部署成本高。
### 方法关键点
1. 提出训练无关的TILT框架，仅在测试阶段通过奖励对齐修正扩散采样轨迹，无需修改基模型权重；
2. 将组合失败归因于联合概念分布与单概念分布的重叠模式，设计完全来自基模型的固有奖励，偏好所有概念同时存在的生成样本；
3. 推导KL约束下的闭式倾斜目标分布，配套两种引导策略，混合策略可平衡两者优势，效果最优。
### 关键结果
在T2ICompBench基准测试上，相比现有基线，组合对齐度显著提升，同时完全保留原有图像生成质量。
