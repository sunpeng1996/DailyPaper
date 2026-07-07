---
title: 'EdgeBench: Unveiling Scaling Laws of Learning from Real-World Environments'
title_zh: EdgeBench：揭示Agent从真实环境学习的缩放定律
authors:
- Deyao Zhu
- Xin Zhou
- Shengling Qin
- Xuekai Zhu
- Hangliang Ding
- Shu Zhong
- Zixin Wen
- Zhonglin Xie
- Chenhui Gou
- Linxuan Ren
affiliations:
- ByteDance
arxiv_id: '2607.05155'
url: https://arxiv.org/abs/2607.05155
pdf_url: https://arxiv.org/pdf/2607.05155
published: '2026-07-05'
collected: '2026-07-07'
category: Agent
direction: Agent环境学习 · 缩放定律与基准构建
tags:
- Agent
- Benchmark
- Scaling Law
- Long-Horizon Task
- Environment Learning
one_liner: 推出含134个长周期真实任务的Agent基准，发现环境学习的log-sigmoid缩放定律及3个月翻倍的增速
practical_value: '- 可复用log-sigmoid缩放定律预测业务Agent（广告优化、选品、文案生成等）的性能天花板和迭代周期，避免盲目投入长周期测试资源

  - EdgeBench的双反馈环设计可直接迁移到业务Agent评估流程：内层本地规则快速校验+外层业务效果终审，兼顾评估效率与准确性

  - 验证了长上下文对长周期任务的稳定增益，落地长会话推荐、用户运营类Agent时优先选择长上下文底座，可降低外部记忆模块的开发成本

  - 参考Agent学习速度每3个月翻番的规律，做业务落地规划时预留半年迭代空间，无需过度纠结当前版本的短期性能上限'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
预训练阶段的缩放定律已被充分验证，但Agent部署后从真实环境交互学习的规律始终不明确。现有基准大多任务周期短、反馈单一，无法支撑长周期环境学习研究，业务中Agent的迭代效果也缺乏可量化的预测依据，亟需统一的评估基准和规律总结。

### 方法关键点
- 构建EdgeBench基准，覆盖134个跨6大类（科学研究、软件工程、组合优化、专业知识工作、形式化数学、交互游戏）的真实任务，单任务支持至少12小时连续运行，平均单任务人类专家投入达57.2小时
- 采用双反馈环设计：内层是Agent驱动的快速本地反馈（编译器、模拟器、本地验证集等），外层是提交触发的权威隐藏评审反馈，完全模拟真实工作流
- 提出环境学习的前沿扩张理论，将学习过程建模为 latent 任务图上的边界扩张，推导得出log-sigmoid函数形式的缩放定律

### 关键结果
- 基于3.8万小时5款前沿Agent交互数据验证，全任务平均的log-sigmoid拟合R²达0.998，跨任务类别、最长72小时长周期、早期数据预测后期性能的场景下拟合精度均≥0.993
- 2025年9月至2026年4月前沿Agent的学习速度每3个月翻番，221天内提升8倍
- 连续积累经验的Agent性能比相同时间预算下独立重启的方案高6.9分（百分制），1M上下文版本比200k版本在12小时任务上性能高4.4分

**最值得记住的一句话**：Agent从真实环境的学习不是随机试错的无序过程，而是存在可预测的量化缩放规律，其增长速度远快于预训练模型的迭代速度。
