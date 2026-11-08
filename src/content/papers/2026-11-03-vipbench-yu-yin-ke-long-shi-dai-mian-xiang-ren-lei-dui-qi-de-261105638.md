---
title: 'VIPBench: A Human-Aligned Benchmark for Voice Identity Perception in the Age
  of Voice Cloning'
title_zh: VIPBench：语音克隆时代面向人类对齐的语音身份感知基准
authors:
- Xudong Tang
- Matthew Groh
affiliations:
- Northwestern University Department of Computer Science
- Kellogg School of Management, Northwestern University
arxiv_id: '2611.05638'
url: https://arxiv.org/abs/2611.05638
pdf_url: https://arxiv.org/pdf/2611.05638
published: '2026-11-03'
collected: '2026-11-08'
category: Eval
direction: 语音模型评估 · 人类感知对齐
tags:
- Benchmark
- Speaker Recognition
- Voice Cloning
- Human Alignment
- Speech Evaluation
one_liner: 发布含12万+人类标注的语音身份感知基准VIPBench，定义4项任务评估语音模型与人类感知的对齐度
practical_value: '- 语音交互Agent（如电商语音客服、语音身份核验模块）可复用VIPBench的4项对齐任务优化模型，降低克隆语音误判风险

  - 语音生成类业务（如AI数字人语音、定制化语音播报）可参考该基准的人类标注逻辑，提升合成语音的用户辨识度

  - 语音模型选型可直接复用核心结论：带说话人标签训练的模型比自监督模型更贴合人类感知，不必过度追求极低的说话人标签错误率'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有说话人识别基准仅基于说话人标签评估准确率，未考虑人类对语音身份的感知差异，无法适配语音克隆普及后的IP保护、安全核验等场景需求。
### 方法关键点
1. 构建VIPBench数据集，包含100位公众人物的9800组语音对（覆盖真实语音、克隆语音、语音融合变体），收集1290名听众的124876条同/异判断标注
2. 定义4项评估任务，分别衡量模型相似度对听众判断的预测能力、模型与人类感知的偏好对齐度、模型对真实/合成语音判断的一致性
### 关键结果数字
41%的听众会将同一说话人的克隆语音与真实语音判定为不同人；最优模型仅能解释61%的可解释方差；带说话人标签训练的模型对齐度优于自监督模型，12%标签错误率的模型与低于2%错误率的模型对齐度相当
