---
title: 'ColorRef: Calibrating Verbal Feedback for Color Revision'
title_zh: ColorRef：面向颜色修正场景的自然语言反馈校准方法
authors:
- Pablo Loyola
- Andres Hoyos-Idrobo
- Edison Marrese-Taylor
- Colin Rowat
- Alfredo Solano
affiliations:
- Rakuten Group, Inc
- The University of Tokyo
arxiv_id: '2611.25653'
url: https://arxiv.org/abs/2611.25653
pdf_url: https://arxiv.org/pdf/2611.25653
published: '2026-11-19'
collected: '2026-11-20'
category: LLM
direction: LLM模糊指令遵循 · 反馈校准
tags:
- LLM Instruction Following
- Feedback Calibration
- Scalar Modifier
- Grounded Language
- Color Revision
one_liner: 通过测量LLM对程度修饰词的实际响应校准反馈措辞，降低颜色修正的步长误差
practical_value: '- 做电商广告素材生成、商品主图定制类Agent时，不要默认LLM对「稍微」「有点」「非常」这类程度副词的响应符合预期，先通过小样本校准集测量每个词在目标Prompt下的实际调整幅度，避免调整过度

  - Agent多轮反馈生成模块不要用通用的程度词映射规则，针对当前调用的基座模型、Prompt模板单独校准措辞，可在不修改模型权重的前提下降低近50%的连续参数调整误差

  - 开发电商智能配色工具（如用户自定义服饰、包装颜色）时，可复用这套校准框架，将用户模糊的自然语言反馈转化为合适的RGB/HSV参数调整幅度，大幅提升交互准确率'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
LLM在处理「再暗一点」「更饱和一点」这类带程度修饰的连续域调整指令时，通常能正确识别调整方向，但步长控制偏差极大，容易出现调整过度/不足的问题。现有对指令遵循的评估仅校验方向是否正确、程度词的相对顺序是否符合逻辑，无法保证实际调整幅度符合需求，在电商素材生成、智能设计Agent等落地场景会严重影响用户体验。

### 方法关键点
- 构建ColorRef颜色参考游戏框架，分离初始颜色语义理解、反馈方向识别、步长响应三个独立环节，采用CIELAB空间的∆E76作为颜色误差度量指标；
- 提出接收方校准策略：先在独立校准集上测量目标LLM对`a little`/`somewhat`/`much`三个程度词搭配不同调整方向的实际中位步长，反馈生成时选择实际步长最接近所需调整量的措辞，全程无需微调模型权重；
- 设计多组对照实验，隔离输出编码格式、固定措辞规则、基座模型差异对调整结果的影响。

### 关键实验结果
- 数据集：1000条众包颜色描述-目标对，32条校准颜色样本，128条held-out测试样本；
- 对比固定程度词阈值规则，校准后Qwen3-14B单步平均误差从12.36降至6.86，Gemma 4 12B从11.06降至5.89，误差降低近48%；
- 3轮带target信息的oracle反馈可将初始颜色预测的平均误差从42.33降至22.15，但仅3.8%的结果达到人眼可接受的误差阈值。

### 核心结论
遵循指令方向、正确排序程度修饰词，与给出符合需求的调整幅度是完全独立的两个能力，反馈效果必须结合接收方的实际响应来评估。
