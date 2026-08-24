---
title: Memory Augmentation Unlocks Efficient Chain-of-Thought Reasoning
title_zh: 内存增强解锁高效思维链推理
authors:
- Simeng Zhang
- Yilong Chen
- Wenyuan Zhang
- Zhenyu Zhang
- Yao Chen
- Junyuan Shang
- Tingwen Liu
affiliations:
- Institute of Information Engineering, CAS
- University of Chinese Academy of Sciences
- Baidu Inc.
- Tencent Inc.
arxiv_id: '2608.21265'
url: https://arxiv.org/abs/2608.21265
pdf_url: https://arxiv.org/pdf/2608.21265
published: '2026-08-21'
collected: '2026-08-24'
category: Reasoning
direction: 思维链推理优化 · 无训练内存增强
tags:
- Chain-of-Thought
- Memory Augmentation
- Inference Acceleration
- CoT Compression
- Training-Free
one_liner: 提出无训练的内存增强压缩框架，压缩CoT推理时兼顾精度，实现1.14~1.49倍推理加速
practical_value: '- 电商Agent复杂推理场景（如优惠计算、用户需求拆解）可复用该思路：将高频推理模式（满减规则、品类计算逻辑）沉淀为离线内存库，线上检索注入prompt，既缩短CoT生成长度降低
  latency，又避免压缩导致的逻辑错误

  - 该框架无需训练即可兼容现有各类CoT压缩、KV cache压缩、TokenSkip等推理优化方案，业务上线成本低，可直接作为现有推理加速方案的补充插件

  - 内存库构建优先提取结构化推理模式/关键约束而非完整样例，检索优先用推理标签匹配而非语义匹配，平衡检索精度与overhead，可复用在推荐query理解、多轮对话意图推理等场景

  - 可参考Context-Generation Substitution Law的权衡公式，根据业务的 latency 容忍度、推理复杂度动态调整注入内存的长度与压缩比例，在精度和速度之间找到最优解'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
CoT是LLM解决复杂任务的核心手段，但长推理链需要逐token生成，带来极高的推理延迟、token成本与服务 overhead；现有CoT压缩方法过度压缩时会丢失逻辑依赖、约束条件，导致精度大幅下降，难以平衡推理效率与效果。

### 方法关键点
- 首次提出Context-Generation Substitution Law，刻画prefill侧推理上下文与解码侧CoT生成的权衡关系：有用的推理上下文可替代部分生成的推理链，当prefill成本小于解码节省的成本时即可获得收益
- 设计无训练的内存增强压缩（MAC）框架，分为离线建库与在线推理两步：离线从历史正确的CoT样例中提取结构化推理内存（包含问题类型、约束、解题策略、关键操作等，而非完整样例），构建内存库；在线先对当前query生成推理标签，检索Top-k相关内存注入prefill上下文，引导模型生成短压缩CoT
- 框架模块化设计，兼容prompt级、token级、KV cache级等各类现有CoT压缩机制，无需修改原有压缩逻辑

### 关键实验
在GSM8K、MATH、BBH、MMLU-Sci等推理数据集上对比CoD（Chain-of-Draft）压缩基线，精度分别提升21.4、28.0、29.5、6.61个百分点，同时相比标准长CoT实现1.14~1.49倍的推理加速；兼容TokenSkip、RPC、Extra-CoT等各类压缩方案，均带来稳定精度提升。

**最值得记住的一句话**：利用prefill的并行计算优势将可复用推理逻辑前置为上下文，是平衡CoT推理精度与延迟的低成本可行路径。
