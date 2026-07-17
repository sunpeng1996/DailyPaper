---
title: WanSong v1.0 Technical Report
title_zh: WanSong v1.0 商用级长歌曲生成技术报告
authors:
- Binghui Chen
- Pandeng Li
- Yu Liu
- Jingren Zhou
affiliations:
- Wan Team, Alibaba Group
arxiv_id: '2607.14749'
url: https://arxiv.org/abs/2607.14749
pdf_url: https://arxiv.org/pdf/2607.14749
published: '2026-07-15'
collected: '2026-07-17'
category: Multimodal
direction: 多模态生成 · 纯扩散长音频生成
tags:
- Diffusion Model
- Audio Generation
- Long-form Generation
- Step Distillation
- Multimodal
one_liner: 纯扩散单阶段架构实现5分钟商用级高保真歌曲生成，支持双音轨输出与高效推理定制
practical_value: '- 可复用纯扩散单阶段架构思路，替换AR+扩散级联管线，提升电商短视频BGM、直播背景音等长内容生成的推理效率与内容一致性

  - step-distillation 蒸馏压缩扩散步数的 trick 可直接迁移到生成类业务的推理优化，大幅降低线上部署的时延与计算成本

  - 单次推理输出多分支结果（人声/伴奏双轨）的设计思路，可复用在多目标生成类业务，减少多模型部署的冗余开销'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有商用音乐生成方案多基于自回归（AR）或AR+扩散级联架构，长音频生成存在推理效率低、全局感知一致性差、可控性不足等痛点，难以满足高质量长歌曲的商用生成需求。
### 方法关键点
摒弃AR主导的多阶段管线，采用纯扩散端到端单阶段架构，将音频直接建模为连续token；以混合MMDit为模型骨干，基于LLM文本描述器做条件控制，文本与音频token拼接为统一序列输入；支持step-distillation步数蒸馏加速推理，提供轻量化微调路径适配下游编辑任务。
### 关键结果
单次推理可直接生成最高5分钟的高保真多语言歌曲，同步输出人声、背景音乐双音轨，达到商用级生成效果。
