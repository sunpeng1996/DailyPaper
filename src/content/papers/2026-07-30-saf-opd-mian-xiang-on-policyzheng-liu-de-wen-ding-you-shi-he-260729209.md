---
title: 'SAF-OPD: Stable Advantage Fusion for On-Policy Distillation'
title_zh: SAF-OPD：面向On-Policy蒸馏的稳定优势融合框架
authors:
- Yifan Ding
- Xincheng Wei
- Yoshua Y. Li
- Ziheng Li
- Yuquan Lu
- Siyu Zhang
- Dongsheng Ma
- Rongxiang Weng
- Xunliang Cai
- Yun Chen
affiliations:
- Shanghai University of Finance and Economics
- Meituan
- The Chinese University of Hong Kong, Shenzhen
- Peking University
arxiv_id: '2607.29209'
url: https://arxiv.org/abs/2607.29209
pdf_url: https://arxiv.org/pdf/2607.29209
published: '2026-07-30'
collected: '2026-08-04'
category: Training
direction: RL训练 · 多优势信号融合优化
tags:
- GRPO
- On-Policy Distillation
- Reinforcement Learning
- LLM Training
- Advantage Fusion
one_liner: 通过四阶段轻量管线控制OPD优势幅度与时序，解决GRPO与OPD固定融合的熵塌陷问题
practical_value: '- 多信号融合（如业务规则奖励+模型蒸馏信号）不要用固定系数，可借鉴幅度+时序双维度控制思路，避免单信号主导导致的训练塌陷

  - 蒸馏信号处理可复用top-k稀疏化+tanh压缩trick，过滤低价值token信号、限制极端值对梯度的干扰，减少训练波动

  - 时序调度可参考KL触发的预热+退火策略，根据模型当前与教师/目标的差距动态调整信号权重，无需提前固定步长，适配不同任务收敛节奏

  - 可直接迁移到推荐系统RL精排训练：把用户点击/转化奖励类比GRPO序列级验证奖励，把专家排序策略/历史优质排序列类比OPD token级教师信号，解决多信号融合的训练不稳定问题'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
RLVR（如GRPO）提供的序列级验证奖励稀疏但可信度高，On-Policy Distillation（OPD）提供的token级教师信号密集但受限于教师能力上限，二者天然互补；但直接用固定系数融合两类优势会触发两个校准问题：一是**幅度不匹配**，无界的OPD优势易出现极端值淹没GRPO信号，二是**时序不匹配**，训练后期全强度OPD会限制模型探索，最终导致熵塌陷、训练提前收敛、性能触顶。
### 方法关键点
仅对OPD优势做四阶段独立可开关的变换，不改动GRPO分支，几乎无额外 overhead：
1. 幅度控制：每序列内保留top-k%高幅度OPD信号、其余置0做稀疏化；再用带系数的tanh压缩，把OPD优势限制在固定区间内，解决幅度不匹配问题
2. 时序控制：先线性预热OPD权重，监测学生与教师的KL散度，下降到预设阈值则提前结束预热；之后随训练步线性退火OPD权重，逐步把训练主导权交还给GRPO，解决时序不匹配问题
### 关键结果
实验以Qwen3-1.7B/4B/8B为学生模型、Qwen3-30B为教师模型，在7个数学推理、代码生成基准测试上，对比GRPO-only、OPD-only、固定系数GRPO+OPD三个基线：SAF在全部6组模型-领域设置下均优于固定融合基线，总得分提升0.51%-2.70%，有效避免了训练早期熵塌陷，保留了模型探索能力，最终性能上限更高。
> 最值得记住：稀疏验证奖励与密集代理信号的融合不能仅依赖单一混合系数，需要分别控制信号的幅度合理性与不同训练阶段的可信度。
