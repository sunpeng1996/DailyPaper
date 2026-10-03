---
title: 'Persona Dosing: Calibrated Activation Steering for Graded Trait Control'
title_zh: 人格剂量控制：面向LLM分级特质控制的校准激活引导方法
authors:
- Zehao Jin
- Junran Wang
- Ruixuan Deng
- Jiahao Chen
- Jingyuan Zhang
- Yuxuan Zhang
- Xinjie Shen
affiliations:
- Georgia Institute of Technology
- Zhejiang University
- University of British Columbia
arxiv_id: '2609.36388'
url: https://arxiv.org/abs/2609.36388
pdf_url: https://arxiv.org/pdf/2609.36388
published: '2026-09-27'
collected: '2026-10-03'
category: LLM
direction: LLM激活引导 · 人格特质分级控制
tags:
- Activation Steering
- Persona Control
- LLM Inference Intervention
- Calibration
- Flow Matching
one_liner: 通过共享特质控制器训练+后训练校准，实现LLM人格特质的分级精准可控且高输出连贯性
practical_value: '- 电商客服/带货Agent人设控制场景可复用「共享控制器训练+后校准映射」架构，无需标注不同强度的训练样本，大幅降低人设适配的数据成本

  - 内容生成/推荐文案生成场景需要分级控制风格强度（如热情度、幽默度、说服度）时，可直接复用剂量-响应曲线校准流程，实现业务侧可解释的强度参数调节

  - 多底座LLM适配场景可参考其校准逻辑，统一上层业务的强度请求接口，自动映射到底层不同模型的控制参数，屏蔽底座差异'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Activation Steering方法的强度参数无实际业务含义，相同参数在不同特质、不同底座LLM上的表现差异极大，既无法精准控制输出指定强度的人格/风格特质，也难以保障输出连贯性，无法落地到对人设稳定性要求高的电商客服、内容生成、Agent交互等场景。
### 方法关键点
- 基于FLAS激活场架构训练共享特质控制器，通过描述条件的速度场变换冻结LLM隐层状态，用flow time控制干预强度；训练仅需特质表达得分≥50的响应样本，无需配对不同强度的标注数据
- 后训练阶段在校准集上测量剂量-响应曲线，用保序回归拟合后做逆向映射，将业务侧请求的0-100分特质强度值直接转换为对应的flow time参数
- 7类人格特质共享同一控制器，切换特质无需加载新适配器，仅需更新特质描述和对应的校准映射
### 关键结果
在Llama-3.1-8B、Qwen3-8B、Gemma-3-4B三个底座上测试，对比CAA、RepE等基线：
1. 连贯性≥75分的约束下，核心特质表达得分分别比CAA高33.2、18.3、17.8分
2. 7类特质的分级强度请求平均MAE仅4.7~6.2分，每款模型可支持14~22个可达强度目标
3. 控制器更新后仅需重新校准曲线即可恢复精准控制，无需重新训练全量参数
### 核心结论
LLM行为控制可拆解为「行为能力训练」和「强度校准」两个独立步骤，在不增加训练成本的前提下大幅提升业务侧可控性
