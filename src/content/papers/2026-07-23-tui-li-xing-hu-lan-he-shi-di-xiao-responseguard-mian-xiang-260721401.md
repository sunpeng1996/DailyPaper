---
title: 'When Are Reasoning-Based Guardrails Not Efficient? ResponseGuard: A Fast Vision-Language
  Guard for Real-Time Moderation'
title_zh: 推理型护栏何时低效？ResponseGuard：面向实时审核的快速多模态安全护栏
authors:
- Dongbin Na
affiliations:
- POSTECH (浦项科技大学)
arxiv_id: '2607.21401'
url: https://arxiv.org/abs/2607.21401
pdf_url: https://arxiv.org/pdf/2607.21401
published: '2026-07-23'
collected: '2026-07-24'
category: LLM
direction: 多模态大模型 · 实时安全审核
tags:
- Vision-Language Model
- Safety Guardrail
- Real-Time Moderation
- Chain-of-Thought
- Inference Optimization
one_liner: 提出无推理单前向传播多模态安全护栏ResponseGuard，响应审核性能更优且速度快150倍
practical_value: '- 电商多模态Agent、导购大模型的实时响应审核可直接复用单前向传播架构，替换推理型护栏大幅降低延迟

  - 流式生成场景可采用逐句检测逻辑，在有害内容完全生成前拦截，避免不良内容暴露给用户

  - 若业务核心需求是审核模型生成的响应而非用户输入请求，优先选用无推理轻量护栏，兼顾性能与成本

  - 多模态审核场景若图像识别精度不足，优先优化视觉编码器而非增加推理步骤，投入产出比更高'
score: 7
source: arxiv-cs.CV
depth: abstract
---

### 动机
当前多模态安全护栏普遍采用CoT推理流程，需解码大量token才能输出有害性判定，延迟极高，无法匹配大模型流式输出的实时审核需求，且推理步骤对审核性能的增益尚未被验证。
### 方法关键点
采用无推理单前向传播架构，将用户请求、模型响应、关联图像的特征池化后直接输出判定结果，无需生成推理链；支持流式场景下逐句检测，可在有害响应完全生成前完成拦截。
### 关键结果
2B参数的ResponseGuard在响应有害性检测任务上效果优于3B参数的推理型多模态护栏，推理速度提升150倍；仅在用户请求有害性检测、纯图像审核场景下推理型护栏仍有优势，性能差距主要源于冻结的视觉编码器而非缺少推理步骤，且推理型护栏的判定几乎不关注图像特征。
