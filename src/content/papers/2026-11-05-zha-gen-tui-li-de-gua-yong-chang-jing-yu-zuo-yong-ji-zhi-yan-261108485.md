---
title: Where and Why is Grounded Reasoning Useful?
title_zh: 扎根推理的适用场景与作用机制研究
authors:
- David Yan
- Le Xue
- Forrest Huang
- Qiuyi Zhang
- Dustin Tran
- Andrew M. Dai
- Yinfei Yang
affiliations:
- Elorian
- Princeton University
arxiv_id: '2611.08485'
url: https://arxiv.org/abs/2611.08485
pdf_url: https://arxiv.org/pdf/2611.08485
published: '2026-11-05'
collected: '2026-11-07'
category: Reasoning
direction: 多模态扎根推理适用边界研究
tags:
- Grounded Reasoning
- VLM
- Chain-of-Thought
- Visual Reasoning
- Benchmark
one_liner: 明确基于坐标的扎根推理适用边界，推出需不可描述视觉参考的新基准BrickVision
practical_value: '- 搭建电商多模态Agent（商品图文理解、直播内容识别等）时，仅当任务涉及不可用文本描述的视觉特征（密集同款计数、不规则纹理匹配等）时才引入坐标扎根推理，避免不必要的架构复杂度

  - 优化VLM推理链路时，可先判断任务是否存在不可描述视觉参考，按需开启grounding能力，降低推理耗时、提升KV cache利用率

  - 自研多模态任务评测基准时，可参考BrickVision的设计思路，补充现有基准未覆盖的不可描述参考场景，提升评测结果的业务适配性'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
基于坐标输出的扎根推理是VLM解决复杂视觉推理任务的常用方案，但此前其收益边界、适用场景及背后逻辑缺乏系统性研究，现有视觉推理基准普遍仅覆盖可通过文本描述的参考场景。
### 方法关键点
1. 提出思维链分析方法，可量化模型推理链路中对输出的grounding坐标信息的实际依赖程度
2. 对扎根推理全训练流程做消融实验，结合多个合成任务验证不同场景下的效果差异
3. 构造BrickVision新基准，专门覆盖需不可描述视觉参考才能解决的任务场景
### 关键结果
计数类任务上扎根推理相比无坐标基线有明确提升；其余绝大多数空间推理、感知类基准上无显著收益；仅当任务需无法用语言描述的视觉参考时，扎根推理性能显著优于纯文本推理。
