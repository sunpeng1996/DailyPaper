---
title: Should We Type or Talk to LLM Agents? A Comprehensive Study of Voice and Keyboard
  Input Perturbations
title_zh: 语音 vs 键盘输入：LLM Agent输入扰动影响的全面研究
authors:
- Zizhao Hu
- Nathan Elijah Segura
- Mohammad Rostami
- Jesse Thomason
affiliations:
- University of Southern California
- Santa Monica College
- Information Sciences Institute, USC
arxiv_id: '2608.03970'
url: https://arxiv.org/abs/2608.03970
pdf_url: https://arxiv.org/pdf/2608.03970
published: '2026-08-04'
collected: '2026-08-05'
category: Eval
direction: LLM Agent 输入鲁棒性评估
tags:
- Input Robustness
- Perturbation Benchmark
- Voice Interaction
- ASR Error
- LLM Evaluation
one_liner: 构建HIVE扰动套件，量化语音/键盘输入扰动对LLM Agent的性能影响并给出7项核心结论
practical_value: '- 搭建语音交互类Agent（如电商语音导购、语音搜索）时，禁止对用户语音转录结果做过度压缩/重写，仅做最小程度的填充词删除即可，过度改写最高会导致任务准确率下降24个百分点

  - 处理用户键盘输入query（搜索、咨询场景）时，无需投入过多资源做低烈度拼写纠错，LLM可吸收12%以内带拼写错误的输入，开启推理模式后可几乎完全消弭键盘输入错误的影响

  - 不要尝试用LoRA等轻量微调方案解决输入扰动导致的性能下降，实验验证轻量微调要么无法修复扰动损失，要么会拉低干净输入下的基线性能

  - 多选择类交互任务（如商品属性选择、分类问答）对输入扰动容忍度极高，语音与键盘输入的性能差距可忽略，这类场景可放心开放语音输入'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
用户与LLM Agent的交互核心依赖键盘、语音两大输入渠道，两类输入均会产生原生系统性扰动：键盘输入的拼写错误、语音输入的转录误差与AI前置改写。现有研究仅覆盖零散扰动类型，未对比两类渠道的真实影响差异，也未给出生产环境可落地的优化依据。

### 方法关键点
- 搭建HIVE扰动生成引擎，包含11种真实语音转录扰动（填充词注入、同音替换、转录改写等）、6种QWERTY键盘输入扰动（邻键错打、字母换位、漏空格等），以及2组对照算子，完全复现普通用户的输入错误模式。
- 所有实验采用配对对照设计，同一干净样本的不同扰动版本在相同模型、解码参数下测试，排除采样噪声、测试集污染等干扰因素。

### 关键实验结果
在GSM8K、HumanEval、MMLU-Pro等6个基准数据集上测试5款主流开源指令微调模型，核心结果：语音转录扰动平均拉低准确率9.7个百分点，其中过度压缩改写最高导致24.1个百分点的准确率损失，填充词仅贡献不到30%的损失；键盘扰动平均仅损失3个百分点，12%以内单词带错的输入几乎不影响性能；仅生成/推理类任务存在两类输入的性能差距，多选类任务差距可忽略；开启模型推理（thinking）模式可完全修复键盘扰动损失，但对语音扰动无效；轻量LoRA微调无法修复输入扰动带来的性能损失。

### 最值得记住的结论
对语音转录结果的过度改写是输入侧最大的性能损失源，影响远高于拼写错误、填充词等常见扰动。
