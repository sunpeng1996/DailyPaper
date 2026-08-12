---
title: 'Ex-Omni-2D: Expressive Omni-Modal Dialogue Models with Native Visual Presence'
title_zh: Ex-Omni-2D：具备原生视觉输出能力的高表现力全模态对话模型
authors:
- Haoyu Zhang
- Zhipeng Li
- Xiaoying Tang
- Tianshu Yu
- Yiwen Guo
affiliations:
- The Chinese University of Hong Kong, Shenzhen
- LIGHTSPEED
- Independent Researcher
arxiv_id: '2608.10720'
url: https://arxiv.org/abs/2608.10720
pdf_url: https://arxiv.org/pdf/2608.10720
published: '2026-08-10'
collected: '2026-08-12'
category: Multimodal
direction: 全模态对话 · 多模态响应生成
tags:
- Omni-modal Dialogue
- Multi-modal Generation
- Streaming Inference
- Knowledge Distillation
- Video Generation
one_liner: 提出全模态对话框架，可同步生成协调的文本、个性化语音及参考条件化视频响应
practical_value: '- 电商虚拟人带货、智能客服Agent场景可复用共享声时接口设计，无需强对齐的query-文本-语音-视频标注即可同步生成口型匹配的多模态响应，大幅降低标注成本

  - 长时序流式生成场景（如直播、长对话）可借鉴Prefix Streaming机制，跨生成块传递干净隐变量，有效降低长序列生成的累计质量衰减

  - 多模态大模型部署可复用Teacher-Student蒸馏方案，将全序列生成器蒸馏为少步流式生成器，在效果损失可控的前提下大幅提升推理速度，满足实时交互要求'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有全模态对话模型仅可输出文本、语音响应，缺少匹配对话语义的原生视觉输出，且同步生成多模态响应需大规模query-text-speech-video对齐标注，落地成本极高。
### 方法关键点
1. 引入结构化Visual Thought Plan (VTP)先预测场景、情绪、动作，再生成响应文本与多码本语音单元；该单元作为共享声时接口，可同时解码为语音、对齐视频帧，支持从异构语音、对话、avatar视频数据训练，无需强对齐四元标注。
2. 以全序列视频生成器为Teacher，蒸馏得到少步块因果Streaming Student，通过Prefix Streaming机制跨块传递干净隐变量，降低长序列生成的累计误差。
### 关键结果
4步推理、4GPU流水线部署下，400×720 / 720×400分辨率的端到端RTF达1.293，实现生成质量与效率的平衡
