---
title: 'Auditing the Judge: Human-Derived Bias Discovery, Quantification, and Mitigation
  in LLM Judges'
title_zh: 面向LLM裁判的人类衍生偏差发现、量化与统一缓解框架
authors:
- Hamin Koo
- Chanjoo Jung
- Fangzhao Wu
- Jaehyung Kim
affiliations:
- Yonsei University
- Microsoft Research Asia
arxiv_id: '2611.33065'
url: https://arxiv.org/abs/2611.33065
pdf_url: https://arxiv.org/pdf/2611.33065
published: '2026-11-24'
collected: '2026-11-25'
category: Eval
direction: LLM评估 · 偏差审计与缓解
tags:
- LLM-as-a-Judge
- Bias Detection
- Bias Mitigation
- Human Preference Alignment
- Evaluation
one_liner: 提出无预定义偏差依赖的HUB-J框架，自动发现、量化并缓解LLM-as-a-Judge的人类对齐偏差
practical_value: '- 生成式推荐/Agent文案自动评估场景可复用偏差识别流程：基于人工标注与LLM评估的分歧case自动挖掘偏差维度，无需人工预定义偏差列表，大幅降低评估体系搭建成本

  - 可复用偏差量化方法诊断业务评估漏洞：将偏差拆解为1-5级可控强度（如文案列表长度、专业术语密度）注入低分候选，统计LLM评估翻转率即可量化当前评估模型对各偏差的敏感度

  - 轻量无训练的偏差缓解方案可直接落地线上链路：通过回归将LLM裁判的预测拆解为基准分与偏差贡献分，移除偏差项即可得到更对齐人类偏好的评估结果，无需重训评估模型'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

## 动机
LLM-as-a-Judge已广泛应用于生成式推荐文案评估、Agent响应质量打分、RLHF偏好标注等业务链路，但现有偏差检测方法依赖预定义偏差列表，无法量化偏差强度，缓解方案多需重训LLM、成本高，且未锚定人类与LLM的真实评估分歧，导致评估结果与人类偏好对齐度低，直接影响生成内容质量、推荐排序效果。

## 方法关键点
- 偏差识别：从多LLM裁判一致、但与人类标注分歧的case中抽取特征，聚类得到可解释的偏差因子，无需预定义偏差列表，可覆盖已知及未知偏差
- 偏差量化：将每个偏差因子拆解为1-5级强度梯度，在人和LLM评估一致的case中，给被拒绝的回复注入不同强度的偏差，统计评估翻转率，得到每个LLM裁判的专属偏差敏感度画像
- 偏差缓解：用轻量回归模型将裁判预测拆解为基准偏好、偏差敏感度、query效应三部分，移除偏差项即可得到无偏评估结果，无需重训LLM裁判

## 关键结果
实验基于合并MT-Bench、WebGPT等5个公开人类偏好数据集，对比预定义偏差集、BiasScope两个基线：识别的偏差平均解释力较预定义偏差高101.7%、较BiasScope高55.8%；偏差缓解阶段平均纠正31.8%的偏差导致的评估翻转，效果泛化到5个不同厂商的LLM裁判均稳定有效。

最值得记住的一句话：LLM裁判的偏差挖掘必须锚定人类和LLM的真实评估分歧，而非预定义的偏差列表，才能真正提升评估的人类对齐度。
