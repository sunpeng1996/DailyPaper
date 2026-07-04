---
title: Reasoning LLM Improves Speaker Recognition in Long-form TV Dramas
title_zh: 推理大模型提升长剧集场景下的说话人识别效果
authors:
- Yuxuan Li
- Lingxi Xie
- Xinyue Huo
- Jihao Qiu
- Jiacheng Shao
- Pengfei Chen
- Jiannan Ge
- Kaiwen Duan
- Qi Tian
affiliations:
- Tsinghua University
- Huawei Inc.
- University of Chinese Academy of Sciences
- Guangdong Laboratory of Artificial Intelligence and Digital Economy (SZ)
arxiv_id: '2607.02504'
url: https://arxiv.org/abs/2607.02504
pdf_url: https://arxiv.org/pdf/2607.02504
published: '2026-07-02'
collected: '2026-07-04'
category: Multimodal
direction: 多模态理解 · 长视频说话人识别
tags:
- Multimodal LLM
- Speaker Recognition
- Long-form Video
- Tool Learning
- Reasoning LLM
one_liner: 构建532K长剧集说话人识别基准，提出基于推理LLM的多模态工具调用方法，效果显著优于现有基线
practical_value: '- 多模态业务场景（如直播内容理解、短视频标签生成）中若单一模态输入质量不稳定（如短语音、模糊画面），可参考用推理LLM调用多模态工具聚合上下文证据补全信息，提升识别准确率

  - 长序列理解类任务（如长用户行为序列建模、长视频内容结构化）可复用其多源证据融合的推理框架设计，降低单一特征输入的鲁棒性风险

  - 垂类场景的benchmark构建可参考其思路，重点覆盖跨模态输入、长尾case（如短语音、低质内容）的标注要求，支撑技术迭代的客观评估'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
长剧集理解高度依赖说话人识别能力，现有方案无法适配剧集多角色、短占比语音等复杂场景，同时缺乏大规模标注基准支撑技术迭代。
### 方法关键点
1. 发布DramaSR-532K大规模基准，覆盖900+独立角色、532K条标注对话，要求融合听觉、语言、视觉多模态cue完成说话人识别任务
2. 提出DramaSR-LRM方案，基于推理大模型（LRM）实现多模态工具自主调用，自动聚合上下文证据、融合多源输入完成高保真说话人归属
### 关键结果
效果显著优于所有现有基线，尤其在声学生物特征固有不可靠的短语音场景优势突出，所有数据与代码已开源。
