---
title: 'Ambient @ EgoLongQA 2026: Distilling Long-Video perception into a Sub-2B Model'
title_zh: Ambient@EgoLongQA2026：将长视频感知蒸馏到20亿参数以下模型
authors:
- Logesh Kumar Umapathi
affiliations:
- TeamAmbient
arxiv_id: '2609.07154'
url: https://arxiv.org/abs/2609.07154
pdf_url: https://arxiv.org/pdf/2609.07154
published: '2026-09-09'
collected: '2026-09-15'
category: Training
direction: 知识蒸馏 · Agent模块轻量化部署
tags:
- Knowledge Distillation
- Model Compression
- Multimodal LLM
- Agent
- Video QA
one_liner: 通过蒸馏Agent感知模块得到1.99B参数长视频问答模型，获ECCV2026竞赛2B参数组第一
practical_value: '- 蒸馏Agent pipeline的特定功能模块（而非全链路Agent）可大幅降低性能损耗，可复用在电商端侧轻量Agent、短视频内容理解小模型的训练中，仅用大Agent正确预测轨迹做蒸馏，性价比极高

  - 裁剪多语言/多语义embedding表的冗余维度，可在不影响保留场景logits输出一致性的前提下压缩参数量，适配端侧推荐、搜索等对模型大小有严格限制的部署场景

  - 单pass小模型可替代多轮工具调用Agent完成高频简单任务，大幅降低推理时延，适合电商短视频商品标签生成、用户意图理解等高吞吐场景'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
长 egocentric 视频多跳问答场景下，带检索工具调用的多轮Agent pipeline精度达81.4%，但参数量过大，无法适配2B参数以下的轻量化部署要求，直接蒸馏全链路Agent会损失过多性能。
### 方法关键点
1. 选择蒸馏Agent pipeline的初级感知模块而非全链路Agent，仅过滤使用大Agent回答正确的轨迹样本训练小参数学生模型；
2. 针对初始2.21B backbone超参数限制的问题，裁剪多语言embedding表从248320行到143469行，保留行的logits输出完全一致。
### 关键结果
最终得到1.9985B参数的单forward pass视觉语言模型，获ECCV 2026 EgoLongQA竞赛<=2B参数组第一名，测试集精度0.8279；仅用大Agent 1.1%的参数量达到其89%的精度，基线模型精度从27.1%提升至81.4%
