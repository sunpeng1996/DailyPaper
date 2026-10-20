---
title: 'Copying Under Repetition: From Prefix Matching to Position Hashing'
title_zh: 重复场景下的序列复制：从前缀匹配到位置哈希编码
authors:
- Anxin Guo
- Tianlong Huang
- Chenxiao Yang
- Zhiyuan Li
affiliations:
- Northwestern University
- Duke University
- Toyota Technological Institute at Chicago
arxiv_id: '2610.26722'
url: https://arxiv.org/abs/2610.26722
pdf_url: https://arxiv.org/pdf/2610.26722
published: '2026-10-19'
collected: '2026-10-20'
category: LLM
direction: 大语言模型 · 位置编码优化
tags:
- Positional Encoding
- Transformer
- VO-RoPE
- Length Generalization
- Finite Precision
one_liner: 采用素数周期VO-Rotation构造2层Transformer，解决重复序列复制的终止误差并证明传统位置编码下界
practical_value: '- 处理长重复内容生成任务（如商品规格复制、客服重复话术输出）可引入VO-RoPE替代传统RoPE/ALiBi，大幅降低重复溢出或提前终止错误

  - 做长度泛化的生成式推荐（如长用户行为序列召回、长文案生成）可参考素数周期模运算+中国剩余定理的位置编码思路，用极少开销实现大跨度位置区分

  - 低精度部署（端侧/边缘侧LLM推理）可复用本文O(log logN)位精度的位置编码设计，在FP8/bf16精度下仍保持稳定位置感知能力'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有前沿LLM复制随机文本准确率接近100%，但处理长重复字符序列时会出现过度生成或提前截断问题；传统基于内容的前缀匹配机制无法区分重复内容的不同位置，常规位置编码（NoPE、ALiBi、RoPE等）在有限精度下无法支撑长重复序列的精准终止，导致复制失败。
### 方法关键点
- 提出基于VO-Rotation的2层Transformer结构，给每个注意力头分配素数周期，通过RoPE风格旋转编码每个位置相对于分隔符（BOS、COPY）偏移量的模素数结果
- 基于中国剩余定理，多个素数周期的模编码联合可区分设计长度N以内的所有偏移量，仅需O(log logN)位精度、O(log N/log logN)宽度即可实现任意重复序列的精准复制与终止
- 证明仅使用最终恒定加性注意力偏差的ECB类Transformer（含NoPE、递归实现的ALiBi等）存在宽度无关的下界：当D(N)2p(N)=o(N)时，无法同时完成长重复序列复制和正确终止
### 关键实验
- 实测GPT-5.5、Gemini 3.1 Pro、Qwen3.5等前沿LLM，长度3000的全相同字符复制任务准确率几乎为0，随机字符串复制准确率接近100%
- 合成实验中，6层512宽的RoPE/ALiBi等基线模型在训练上限2000长度的全相同字符复制任务上准确率低于26%，而2层256宽的VO模型准确率达100%，且可泛化到素数周期乘积5005长度，准确率接近100%
### 核心结论
重复场景下的序列复制瓶颈本质是位置信息的编码问题，而非模型宽度或深度问题，值侧位置编码是解决该问题的高效路径
