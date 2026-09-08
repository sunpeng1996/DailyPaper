---
title: 'PRISM-Bench: An Audio-Centric Diagnostic Benchmark for Text-to-Audio-Video
  Generation'
title_zh: PRISM-Bench：面向文本生成音视频的音频中心型诊断评测基准
authors:
- Yuchen Sun
- Qian Yang
- Jun Wang
- Detai Xin
- Guoqiao Yu
- Guanglu Wan
- Qi Jia
affiliations:
- Shanghai Artificial Intelligence Laboratory
- Meituan
arxiv_id: '2609.04867'
url: https://arxiv.org/abs/2609.04867
pdf_url: https://arxiv.org/pdf/2609.04867
published: '2026-09-04'
collected: '2026-09-08'
category: Eval
direction: 多模态生成 · 音视频生成评测
tags:
- Text-to-Audio-Video
- Multimodal Evaluation
- MLLM-as-a-Judge
- Audio-Visual Grounding
- Benchmark
one_liner: 推出首个音频中心型文本生成音视频评测基准，实现多维度细粒度诊断且判分和人类高度对齐
practical_value: '- 电商短视频/直播AIGC场景可复用其35项音频维度细粒度评测准则，解决音画同步、音频质量等业务评测痛点

  - 多模态内容自动评估可参考其「盲测+与Ground Truth侧对比」的MLLM-as-a-Judge优化方案，提升自动判分和人类主观感受的对齐度

  - 可迁移「按模态属性拆分正交评测轴」的思路，用于商品图文/短视频生成的专项评测体系搭建，快速定位模型缺陷'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有文本生成音视频（T2AV）评测普遍低估音频模态价值，要么将音频作为视频质量的辅助评估项，要么脱离音视对齐关系单独评估音频，无法准确定位模型音频生成的真实缺陷。

### 方法关键点
基于900条人工验证样本搭建基准，沿音频类型（语音/音乐/音效）、声源可见性（On-screen/Off-screen）两个正交轴拆分评测维度，覆盖音视一致性、音频质量、音频表现力、Prompt Following 4个感知维度共35项细粒度指标；采用基于盲测、与真值侧对比较的增强MLLM-as-a-Judge判分协议。

### 关键结果数字
自动判分和人类评估的平均对齐度超70%；实测显示前沿闭源T2AV模型和开源模型性能差距显著，现有范式普遍过拟合感知保真度，在复杂对齐、控制任务上表现较差，尤其是音乐生成、On-screen声源音频同步生成的效果不佳。
