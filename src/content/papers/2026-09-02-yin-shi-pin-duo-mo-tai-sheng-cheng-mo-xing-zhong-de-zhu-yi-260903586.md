---
title: The Attention Triangle in Audio-Video Models
title_zh: 音视频多模态生成模型中的注意力三角机制研究
authors:
- Sagi Polaczek
- Noa Kraicer
- Gal Metzer
- Zhuo Ning
- Ali Mahdavi-Amiri
- Daniel Cohen-Or
- Raja Giryes
affiliations:
- Tel Aviv University
- Simon Fraser University
arxiv_id: '2609.03586'
url: https://arxiv.org/abs/2609.03586
pdf_url: https://arxiv.org/pdf/2609.03586
published: '2026-09-02'
collected: '2026-09-07'
category: Multimodal
direction: 多模态生成 · 跨模态注意力优化
tags:
- Cross-Modal Attention
- Diffusion Model
- Audio-Video Generation
- Semantic Alignment
- Inference Steering
one_liner: 提出文本-音频-视频注意力三角分析框架，解决跨模态语义泄漏问题，提升多模态生成一致性
practical_value: '- 多模态商品短视频生成场景可复用推理阶段注意力干预方法，无需微调即可解决配音、画面、文案语义冲突问题（比如口型不对、商品属性和旁白描述不符），降低内容生产的纠错成本

  - 跨模态搜索召回场景中，可借鉴注意力衍生信号作为多模态语义对齐特征，提升音视频、图文商品的召回排序相关性

  - 多模态Agent的感知模块可引入注意力三角分析逻辑，快速定位跨模态输入的语义冲突，提升环境感知的准确度'
score: 6
source: huggingface-daily
depth: abstract
---

# 动机
音视频扩散模型依赖跨模态注意力协调文本、音频、视频三类模态内容，但该机制会引入系统性语义泄漏，当提示词与模型预训练先验存在冲突时，生成结果常不符合预期（比如提示要求鹦鹉说话，实际生成海盗说话的错误结果）。
# 方法关键点
1. 提出注意力三角分析框架，覆盖文本-音频、文本-视频、音频-视频三条跨注意力边，明确音频-视频边的双向交互是语义泄漏的核心来源，模型预训练编码的偏差会在提示与先验冲突时覆盖指定条件，路由到符合视觉先验的错误结果。
2. 提取注意力衍生信号作为诊断工具定位泄漏路径，在推理阶段对不同注意力边做定向干预，实现多模态语义对齐。
# 关键结果
实验验证该方法可在不降低生成质量的前提下，显著改善跨模态语义对齐效果，有效修正语音归属错误、视觉属性泄漏等典型问题。
