---
title: 'DLoop: Looped Speculative Decoding'
title_zh: DLoop：循环式推测解码实现LLM无损生成加速
authors:
- Geonmo Gu
- Byeongho Heo
- HeeJae Jun
- Yoohoon Kang
- Sangmin Lee
- Sangdoo Yun
- Dongyoon Han
affiliations:
- NAVER AI Lab
- NAVER AI Search Platform
- Korea University
arxiv_id: '2610.07659'
url: https://arxiv.org/abs/2610.07659
pdf_url: https://arxiv.org/pdf/2610.07659
published: '2026-10-05'
collected: '2026-10-08'
category: LLM
direction: LLM推理优化 · 推测解码提速
tags:
- Speculative Decoding
- LLM Inference Acceleration
- Lossless Generation
- Looped Decoding
one_liner: 为各类主流推测解码方法叠加循环逻辑，无额外参数下实现5%-41%无损解码提速
practical_value: '- 现有LLM生成类业务（推荐文案生成、Agent多轮回复、商品标题优化）可直接在现有推测解码管线叠加DLoop逻辑，仅需微调1轮draft模型即可获得5%-40%的生成速度提升，无输出质量损失

  - 推测解码的置信度门控设计可直接复用：用单轮draft token的对数概率和作为判断阈值，无需新增模块，仅需调整超参数g即可平衡速度与准确率，适合业务快速上线

  - 循环感知训练的思路可迁移到多步生成类任务：当模型需要基于自身未验证的输出继续生成时，训练时引入自身历史隐藏状态的多轮unroll，可大幅降低分布偏移'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有推测解码每次draft后必须执行一次大模型验证，即使draft结果100%被接受也无法跳过验证，造成大量高成本大模型前向传播浪费；已有自适应draft长度方法仅支持自回归draft模型，无法适配近年流行的并行draft模型；且多轮draft时draft模型依赖未验证token的大模型隐藏状态，训练分布与推理分布不匹配导致生成准确率下降。

### 方法关键点
- 置信度门控draft循环：每次draft完成后计算该轮所有draft token的对数概率和，高于阈值g则继续下一轮draft，低于阈值则统一验证所有累积draft token，无需新增模块，计算开销可忽略
- 循环感知训练：训练时随机采样循环深度S，让draft模型基于自身前序轮次的隐藏状态生成后续draft token，仅对首轮和最后一轮draft计算交叉熵损失，无需修改模型架构、无额外参数
- 兼容所有主流推测解码框架（EAGLE-3、DFlash、Domino、DSpark等）和树验证逻辑，完全保留原解码的无损特性

### 关键实验
基于Qwen3-4B/8B、Qwen3.5-9B、Gemma-4-12B等主流开源模型，在数学、代码、对话三类共8个benchmark上验证，对比原生推测解码：平均接受长度提升12%-102%，墙钟速度提升5%-41%；叠加树验证后仍能额外提速7%-25%；低并发场景下SGLang serving吞吐量最高提升12%。

### 核心结论
用极低成本的小模型多轮前向替换高成本的大模型验证前向，是LLM生成提速的核心性价比逻辑。
