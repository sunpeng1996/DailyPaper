---
title: 'Hy-MT3: More Accurate, Robust and Practical Multilingual Translation Models
  in the Wild'
title_zh: Hy-MT3：面向真实场景的高精准鲁棒多语种翻译模型家族
authors:
- Mao Zheng
- Zheng Li
- Fangxu Liu
- Tao Chen
- Bingxin Qu
- Bo Lv
- Mingrui Sun
- Hongyu Li
- Hong Huang
- Jinlong Song
affiliations:
- Tencent Hunyuan Team
- Honor of Kings Team
arxiv_id: '2611.27673'
url: https://arxiv.org/abs/2611.27673
pdf_url: https://arxiv.org/pdf/2611.27673
published: '2026-11-20'
collected: '2026-11-23'
category: LLM
direction: 多语种大模型 · 翻译与自动评测
tags:
- Machine Translation
- MoE
- Multilingual LLM
- Automatic Evaluation
- Low-resource Language
one_liner: 推出3种参数量的多语种翻译模型家族，支持102种语言，开源细粒度翻译评测工具TransRubric
practical_value: '- 跨境电商/多语种推荐场景可直接复用Hy-MT3轻量模型：1.8B/7B模型精度超过微软、讯飞等商用翻译API，支持102种语言覆盖小语种用户需求，推理延迟低适合实时翻译商品详情、用户评论、海外广告文案

  - TransRubric细粒度评测方法可迁移到生成式推荐/Agent的输出质量评估：按业务场景自定义错误类型（幻觉、术语错误、格式错误等），自动打分量稳定性是人工的4.7倍，可大幅降低人工标注成本

  - 垂直场景约束对齐思路可复用：游戏场景的术语/占位符保留优化方法，可直接套用到电商商品属性、营销文案的固定术语/动态占位符保留场景，降低输出错误率和人工校验成本

  - MoE小激活参数选型思路可复用：3B激活参数的MoE模型性能超过30倍计算量的稠密大模型，适合对推理 latency、成本要求高的实时多语种文案生成、用户Query翻译等场景'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
前序Hy-MT2落地时暴露四大痛点：真实场景翻译忠实度不足（56%样本存在错译、21%存在漏译/增译），仅支持38种语言无法覆盖小语种长尾需求，游戏本地化、OCR级图像翻译等垂直场景的特殊约束（占位符保留、OCR错误容忍）未被优化，传统翻译评测指标与人工判断一致性差，无法区分强模型的细粒度差异。

### 方法关键点
- 模型系列：包含1.8B/7B稠密模型、30B-A3B MoE模型（仅3B激活参数），补充大量低资源语言语料，支持语言从38种扩展到102种
- 垂直场景优化：游戏场景联合王者荣耀团队引入高质量领域语料+专属评测体系，优化占位符/富文本标签/术语一致性；图像翻译场景强化上下文纠错能力，可容忍OCR识别错误
- 开源TransRubric评测工具：基于LLM-as-judge框架，按错误类型（准确性、完整性、术语、指令遵循）和严重度打分，支持有/无参考两种模式，和人工判断一致性更高

### 关键结果
- 通用翻译：30B-A3B在非思考模式下所有评测集均为SOTA，TransRubric平均得分88.5，超过Qwen3.8-Max、Kimi-K3.1-Pro等模型，性能接近GPT-6.1-Sol等思考模式闭源模型，推理成本仅为后者1/30；相比Hy-MT2，错译率降43%、漏增译降74%、指令遵循错误降40%
- 垂直场景：游戏翻译人工评分89.6，超过Gemini 3.1 Pro等闭源模型，术语错误率仅0.08%；OCR级图像翻译得分45.73，为同规模模型SOTA
- 评测工具：TransRubric在WMT26评测任务上平均相关度0.832，超过所有参评方案，打分稳定性是人类标注的4.7倍

> 最值得记住：3B激活参数的MoE翻译模型即可超过多数千亿级稠密大模型的翻译效果，细粒度rubric式自动评测是对齐生成效果和人工需求的核心工具
