---
title: 'ReTerm: Recovery Training for Self-Improving Terminal Agents'
title_zh: ReTerm：面向自改进终端智能体的错误恢复训练框架
authors:
- Wei Xie
- Kaituo Feng
- Shiming Fu
- Yong Liu
- Xiangyu Yue
- Shuangjia Zheng
affiliations:
- Fudan University
- MMLab, The Chinese University of Hong Kong
- Shanghai Jiao Tong University
arxiv_id: '2610.18484'
url: https://arxiv.org/abs/2610.18484
pdf_url: https://arxiv.org/pdf/2610.18484
published: '2026-10-12'
collected: '2026-10-14'
category: Agent
direction: Agent 错误恢复与自优化训练
tags:
- Terminal Agent
- GRPO
- Reinforcement Learning
- Self-Correction
- SFT
one_liner: 通过专属恢复数据集和改进GRPO算法，大幅提升终端Agent从自身执行错误中恢复的能力
practical_value: '- 做交互类Agent（如电商客服Agent、用户运营执行Agent）时，可复用ReTerm的失败轨迹数据构建流程：先收集自身模型执行失败的状态快照，再用强teacher生成高质量恢复轨迹做SFT冷启动，比人工构造错误样本更贴合真实错误分布

  - 做Agent的RL优化时，可借鉴ReTerm-GRPO的设计：新增失败状态任务队列，存储近期策略产生的失败任务，和原任务一起做联合优化，让错误恢复能力与任务解决能力协同进化，避免固定SFT数据集的分布偏移问题

  - 针对多轮交互的推荐/广告Agent的自我修正场景，可复用论文的4步轨迹过滤策略（验证通过、格式合规、符合约束、无无效循环）筛选高质量修正样本，降低训练噪声'
score: 9
source: huggingface-daily
depth: full_pdf
---

### 动机
现有终端Agent在长周期执行任务时频繁遇到命令错误、实现缺陷等问题，无法自主恢复最终导致任务失败；现有通过人工注入错误生成恢复样本的方法与模型真实产生的错误分布不匹配，且仅靠SFT无法充分释放RL的优化潜力。
### 方法关键点
- 数据层：构建ReTerm-10K高质量恢复数据集，先运行Base模型收集失败轨迹与环境快照，用强教师模型生成恢复路径，经4步过滤（验证通过、格式合规、符合约束、无无效循环）保留1万条优质样本用于SFT冷启动
- 算法层：提出ReTerm-GRPO在线RL算法，从当前策略的失败状态分叉生成多组独立恢复尝试，基于验证结果生成组相对奖励优化恢复行为；新增恢复任务队列，优先存储和采样近期策略产生的失败任务，避免分布偏移，与原任务联合优化
- 训练策略：先做恢复定向SFT，再用ReTerm-GRPO做RL迭代，损失仅计算恢复段的token，忽略其他上下文token
### 关键实验结果
基于Qwen3.5-9B训练的ReTerm-9B，在Terminal-Bench 2.0上Pass@1达34.8%，较Base模型提升14.6个点，较标准GRPO训练提升6.8个点；在SWE-bench Verified上Pass@1达58.4%，较Base提升13.2个点；跨4种不同Agent交互框架、跨数学推理、表格操作等域外任务均取得一致增益，所有错误类型的恢复率均高于标准GRPO。
### 核心结论
针对交互类Agent的性能优化，除提升单次任务执行能力外，针对性优化自身错误恢复能力可带来同等甚至更高的收益，且能力可跨场景迁移
